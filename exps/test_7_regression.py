from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["spa"],
        "datasets" : ["lucas_full"],
        "target_sizes" : [15, 20, 25, 30]
    }
    ev = Evaluator(tasks,1,1,"test_7_regression.csv")
    ev.evaluate()