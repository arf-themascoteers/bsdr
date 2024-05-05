from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr","bsnet"],
        "datasets" : ["lucas_downsampled_min"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = Evaluator(tasks,1,10,"bsnet.csv",skip_all_bands=True)
    ev.evaluate()