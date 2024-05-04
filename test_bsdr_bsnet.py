from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["fsdrl","bsnet"],
        "datasets" : ["lucas_full","lucas_downsampled"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = Evaluator(tasks,1,10,"bsnet.csv",skip_all_bands=True)
    ev.evaluate()