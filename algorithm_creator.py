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
from algorithms.algorithm_bsdr5 import AlgorithmBSDR5
from algorithms.algorithm_bsdr6 import AlgorithmBSDR6
from algorithms.algorithm_bsdr7 import AlgorithmBSDR7
from algorithms.algorithm_bsdr8 import AlgorithmBSDR8
from algorithms.algorithm_bsdr9 import AlgorithmBSDR9
from algorithms.algorithm_bsdr10 import AlgorithmBSDR10
from algorithms.algorithm_bsdr11 import AlgorithmBSDR11


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
            "bsdr4" : AlgorithmBSDR4,
            "bsdr5" : AlgorithmBSDR5,
            "bsdr6" : AlgorithmBSDR6,
            "bsdr7" : AlgorithmBSDR7,
            "bsdr8" : AlgorithmBSDR8,
            "bsdr9" : AlgorithmBSDR9,
            "bsdr10" : AlgorithmBSDR10,
            "bsdr11" : AlgorithmBSDR11
        }

        if name not in algorithms:
            raise KeyError(f"No algorithm named {name} exists")

        if name in ["bsdr","bsdr1","bsdr2","bsdr3","bsdr4", "bsdr5", "bsdr6","bsdr7","bsdr8","bsdr9","bsdr10","bsdr11","rec"]:
            return algorithms[name](target_size, splits, repeat, fold, verbose=verbose)

        return algorithms[name](target_size, splits)