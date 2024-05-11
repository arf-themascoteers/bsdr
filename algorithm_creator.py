from algorithms.algorithm_lasso import AlgorithmLasso
from algorithms.algorithm_spa import AlgorithmSPA
from algorithms.algorithm_mcuve import AlgorithmMCUVE
from algorithms.algorithm_pcal import AlgorithmPCALoading

from algorithms.algorithm_bsnet import AlgorithmBSNet
from algorithms.algorithm_zhang import AlgorithmZhang
from algorithms.algorithm_bsdr import AlgorithmBSDR

from algorithms.algorithm_reconstructor import AlgorithmReconstructor

from algorithms.algorithm_bsdr1 import AlgorithmBSDR1
from algorithms.algorithm_bsdr2 import AlgorithmBSDR2
from algorithms.algorithm_bsdr3 import AlgorithmBSDR3
from algorithms.algorithm_bsdr4 import AlgorithmBSDR4


class AlgorithmCreator:
    @staticmethod
    def create(name, target_size, splits, repeat, fold, verbose=True):

        algorithms = {
            "lasso" : AlgorithmLasso,
            "spa" : AlgorithmSPA,
            "mcuve" : AlgorithmMCUVE,
            "pcal" : AlgorithmPCALoading,
            "bsnet" : AlgorithmBSNet,
            "zhang" : AlgorithmZhang,
            "bsdr" : AlgorithmBSDR,
            "rec" : AlgorithmReconstructor,

            "bsdr1" : AlgorithmBSDR1,
            "bsdr2" : AlgorithmBSDR2,
            "bsdr3" : AlgorithmBSDR3,
            "bsdr4" : AlgorithmBSDR4
        }

        if name not in algorithms:
            raise KeyError(f"No algorithm named {name} exists")

        if name in ["bsdr","bsdr1","bsdr2","bsdr3","bsdr4", "rec"]:
            return algorithms[name](target_size, splits, repeat, fold, verbose=verbose)

        return algorithms[name](target_size, splits)