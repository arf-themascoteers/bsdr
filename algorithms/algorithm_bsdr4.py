from algorithms.algorithm_bsdr import AlgorithmBSDR


class AlgorithmBSDR4(AlgorithmBSDR):
    def __init__(self, target_size, splits, repeat, fold, verbose=True, epochs=2000):
        super().__init__(target_size, splits, repeat, fold,[128,64],verbose, epochs)

    def get_name(self):
        return "bsdr4"