from algorithms.algorithm_lasso import AlgorithmLasso
from algorithms.algorithm_spa import AlgorithmSPA
from algorithms.algorithm_mcuve import AlgorithmMCUVE
from algorithms.algorithm_pcal import AlgorithmPCALoading

from algorithms.algorithm_bsnet import AlgorithmBSNet
from algorithms.algorithm_zhang import AlgorithmZhang
from algorithms.algorithm_bsdr import AlgorithmBSDR

from algorithms.algorithm_reconstructor import AlgorithmReconstructor



class AlgorithmCreator:
    @staticmethod
    def create(name, target_size, splits, repeat, fold):

        algorithms = {
            "lasso" : AlgorithmLasso,
            "spa" : AlgorithmSPA,
            "mcuve" : AlgorithmMCUVE,
            "pcal" : AlgorithmPCALoading,
            "bsnet" : AlgorithmBSNet,
            "zhang" : AlgorithmZhang,
            "bsdr" : AlgorithmBSDR,
            "rec" : AlgorithmReconstructor,
        }

        if name not in algorithms:
            raise KeyError(f"No algorithm named {name} exists")

        if name in ["bsdr", "rec"]:
            return algorithms[name](target_size, splits, repeat, fold)

        return algorithms[name](target_size, splits)