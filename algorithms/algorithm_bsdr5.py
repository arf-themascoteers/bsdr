from algorithms.algorithm_bsdr import AlgorithmBSDR


class AlgorithmBSDR5(AlgorithmBSDR):
    def __init__(self, target_size, splits, repeat, fold, verbose=True):
        super().__init__(target_size, splits, repeat, fold,[128,64],verbose, 0)

    def get_name(self):
        return "bsdr5"