from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsnet", "mcuve", "pcal", "lasso"],
        "datasets" : ["indian_pines", "ghisaconus"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = Evaluator(tasks,1,10,"test_3_classification.csv")
    ev.evaluate()