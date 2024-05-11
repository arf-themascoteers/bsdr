from algorithm import Algorithm
from algorithms.bsdr11.bsdr11 import BSDR11
import numpy as np
from ds_manager import DSManager
import torch


class AlgorithmBSDR11(Algorithm):
    def __init__(self, target_size, splits, repeat, fold, structure=None, verbose=True, epochs=4000):
        super().__init__(target_size, splits, repeat, fold)
        torch.manual_seed(1)
        torch.cuda.manual_seed(1)
        torch.backends.cudnn.deterministic = True
        self.verbose = verbose
        self.task = DSManager.get_task_by_dataset_name(splits.get_name())
        class_size = 1
        if self.task == "classification":
            class_size = len(np.unique(self.splits.train_y))
        self.bsdr = BSDR11(self.target_size, class_size, self.splits, self.get_name(), self.repeat, self.fold, [64, 32], self.verbose, epochs)

    def get_selected_indices(self):
        self.bsdr.fit(self.splits.train_x, self.splits.train_y, self.splits.validation_x, self.splits.validation_y)
        return self.bsdr, self.bsdr.get_indices()

    def get_name(self):
        return "bsdr11"