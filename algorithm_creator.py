from algorithms.algorithm_lasso import AlgorithmLasso
from algorithms.algorithm_spa import AlgorithmSPA
from algorithms.algorithm_mcuve import AlgorithmMCUVE
from algorithms.algorithm_pcal import AlgorithmPCALoading

from algorithms.algorithm_bsnet import AlgorithmBSNet
from algorithms.algorithm_zhang import AlgorithmZhang
from algorithms.algorithm_bsdr import AlgorithmBSDR


class AlgorithmCreator:
    @staticmethod
    def create(name, target_size, splits, repeat, fold):
        if name == "bsdr":
            return AlgorithmBSDR(target_size, splits, repeat, fold)

        algorithms = {
            "lasso" : AlgorithmLasso,
            "spa" : AlgorithmSPA,
            "mcuve" : AlgorithmMCUVE,
            "pcal" : AlgorithmPCALoading,
            "bsnet" : AlgorithmBSNet,
            "zhang" : AlgorithmZhang,
            "bsdr" : AlgorithmBSDR
        }

        if name not in algorithms:
            raise KeyError(f"No algorithm named {name} exists")

        return algorithms[name](target_size, splits)