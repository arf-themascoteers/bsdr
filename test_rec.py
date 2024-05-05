from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["rec","bsdr"],
        #"datasets" : ["lucas_full"],
        "datasets" : ["lucas_downsampled_min"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = Evaluator(tasks,1,1,"rec.csv",skip_all_bands=True)
    ev.evaluate()