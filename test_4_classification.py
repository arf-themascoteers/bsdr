from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["spa"],
        "datasets" : ["indian_pines", "ghisa"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = Evaluator(tasks,1,10,"test_4_classification.csv")
    ev.evaluate()