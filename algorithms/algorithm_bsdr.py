from algorithm import Algorithm
from algorithms.bsdr.bsdr import BSDR
import numpy as np
from ds_manager import DSManager
import torch


class AlgorithmBSDR(Algorithm):
    def __init__(self, target_size, splits, repeat, fold, verbose=True):
        super().__init__(target_size, splits, repeat, fold)
        self.verbose = verbose
        self.task = DSManager.get_task_by_dataset_name(splits.get_name())
        torch.manual_seed(1)
        torch.cuda.manual_seed(1)
        torch.backends.cudnn.deterministic = True

    def get_selected_indices(self):
        class_size = 1
        if self.task == "classification":
            class_size = len(np.unique(self.splits.train_y))
        bsdr = BSDR(self.target_size, class_size, self.splits, self.repeat, self.fold, self.verbose)
        bsdr.fit(self.splits.train_x, self.splits.train_y, self.splits.validation_x, self.splits.validation_y)
        return bsdr, bsdr.get_indices()

    def get_name(self):
        return "bsdr"