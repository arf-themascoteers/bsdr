from algorithms.algorithm_bsdr import AlgorithmBSDR


class AlgorithmBSDR1(AlgorithmBSDR):
    def __init__(self, target_size, splits, repeat, fold, verbose=True):
        super().__init__(target_size, splits, repeat, fold)
        self.bsdr.epochs = 1000


    def get_name(self):
        return "bsdr1"