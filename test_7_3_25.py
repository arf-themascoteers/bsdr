from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["spa"],
        "datasets" : ["lucas_full"],
        "target_sizes" : [25]
    }
    ev = Evaluator(tasks,1,1,"7_1_25.csv",skip_all_bands=True)
    ev.evaluate()