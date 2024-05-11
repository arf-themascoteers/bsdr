from algorithms.algorithm_bsdr import AlgorithmBSDR


class AlgorithmBSDR6(AlgorithmBSDR):
    def __init__(self, target_size, splits, repeat, fold, verbose=True):
        super().__init__(target_size, splits, repeat, fold,[265,128,64],verbose, 4000)

    def get_name(self):
        return "bsdr6"