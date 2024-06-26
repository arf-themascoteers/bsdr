from algorithms.algorithm_bsdr import AlgorithmBSDR


class AlgorithmBSDR1(AlgorithmBSDR):
    def __init__(self, target_size, splits, repeat, fold, verbose=True, epochs=2000):
        super().__init__(target_size, splits, repeat, fold,[],verbose, epochs)

    def get_name(self):
        return "bsdr1"