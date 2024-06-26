import torch.nn as nn
import torch


class RecANN(nn.Module):
    def __init__(self, feature_size):
        super().__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.feature_size = feature_size
        self.linear = nn.Sequential(
            nn.Linear(self.feature_size, self.feature_size),
            nn.Sigmoid()
        )

    def forward(self, X):
        return self.linear(X)

    def get_indices(self):
        return torch.sigmoid(self.indices)

