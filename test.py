from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["fsdrl"],
        "datasets" : ["indian_pines"],
        "target_sizes" : [5]
    }
    ev = Evaluator(tasks,1,1,"dummy3.csv",skip_all_bands=True)
    ev.evaluate()