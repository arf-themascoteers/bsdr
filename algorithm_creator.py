from algorithms.algorithm_fscr import AlgorithmFSCR
from algorithms.algorithm_fscrd import AlgorithmFSCRD
from algorithms.algorithm_fscrl import AlgorithmFSCRL
from algorithms.algorithm_lasso import AlgorithmLasso
from algorithms.algorithm_logistic import AlgorithmLogistic
from algorithms.algorithm_cars import AlgorithmCARS
from algorithms.algorithm_spa import AlgorithmSPA
from algorithms.algorithm_mcuve import AlgorithmMCUVE
from algorithms.algorithm_pcal import AlgorithmPCALoading
from algorithms.algorithm_pca import AlgorithmPCA
from algorithms.algorithm_bsnet import AlgorithmBSNet
from algorithms.algorithm_zhang import AlgorithmZhang
from algorithms.algorithm_bsnetcw import AlgorithmBSNetCW
from algorithms.algorithm_bsnetig import AlgorithmBSNetIG
from algorithms.algorithm_bsnetig2 import AlgorithmBSNetIG2


class AlgorithmCreator:
    @staticmethod
    def create(name, target_size, splits):
        if name == "fsdr":
            return AlgorithmFSCR(target_size, splits)
        elif name == "lasso":
            return AlgorithmLasso(target_size, splits)
        elif name == "logistic":
            return AlgorithmLogistic(target_size, splits)
        elif name == "cars":
            return AlgorithmCARS(target_size, splits)
        elif name == "spa":
            return AlgorithmSPA(target_size, splits)
        elif name == "mcuve":
            return AlgorithmMCUVE(target_size, splits)
        elif name == "pcal":
            return AlgorithmPCALoading(target_size, splits)
        elif name == "fsdrd":
            return AlgorithmFSCRD(target_size, splits)
        if name == "fsdrl":
            return AlgorithmFSCRL(target_size, splits)
        elif name == "pca":
            return AlgorithmPCA(target_size, splits)
        elif name == "bsnet":
            return AlgorithmBSNet(target_size, splits)
        elif name == "zhang":
            return AlgorithmZhang(target_size, splits)
        elif name == "bsnetig":
            return AlgorithmBSNetIG(target_size, splits)
        elif name == "bsnetig2":
            return AlgorithmBSNetIG2(target_size, splits)
        elif name == "bsnetcw":
            return AlgorithmBSNetCW(target_size, splits)

