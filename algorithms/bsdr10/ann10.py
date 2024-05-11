import torch.nn as nn
import torch
from collections import OrderedDict
from algorithms.bsdr9.linspacer import get_points


class ANN10(nn.Module):
    def __init__(self, target_size, class_size,structure=None):
        super().__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.target_size = target_size
        self.class_size = class_size
        self.group_size = 10
        init_vals = get_points(0.001, 0.99, self.target_size, 10)
        self.indices = nn.Parameter(torch.tensor([ANN10.inverse_sigmoid_torch(i) for i in init_vals], requires_grad=True).to(self.device))
        if structure == None:
            structure = [128,64]
        self.linear = self.create_structure(structure)
        num_params = sum(p.numel() for p in self.parameters() if p.requires_grad)
        print("Number of learnable parameters:", num_params)


    def create_structure(self, structure):
        if structure == None:
            structure = []
        structure = [self.target_size*self.group_size] + structure + [self.class_size]
        odict = OrderedDict()

        for index in range(len(structure)-1):
            odict['fc' + str(index+1)] = nn.Linear(structure[index], structure[index+1])
            odict['lrelu' + str(index+1)] = nn.LeakyReLU()

        return nn.Sequential(odict)

    @staticmethod
    def inverse_sigmoid_torch(x):
        return -torch.log(1.0 / x - 1.0)

    def forward(self, linterp):
        outputs = linterp(self.get_all_indices())
        # outputs = outputs.view(outputs.shape[0], self.target_size, self.group_size)
        # outputs2 = outputs.mean(dim=2)
        soc_hat = self.linear(outputs)
        if self.class_size == 1:
            soc_hat = soc_hat.reshape(-1)
        return soc_hat

    def get_all_indices(self):
        return torch.sigmoid(self.indices)

    def get_indices(self):
        all_indices = self.get_all_indices()
        indices = torch.stack([torch.mean(all_indices[i*self.group_size:(i*self.group_size)+self.group_size]) for i in range(self.target_size)])
        return indices

    def get_group_loss(self):
        loss = torch.tensor(0.0, dtype=torch.float32).to(self.device)
        for i in range(self.target_size):
            loss = loss + torch.std(self.indices[i:i+self.group_size])
        return loss

