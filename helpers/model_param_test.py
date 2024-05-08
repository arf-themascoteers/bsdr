from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr","bsnet","zhang"],
        "datasets" : ["ghisaconus","indian_pines"],
        "target_sizes" : [5]
    }
    ev = Evaluator(tasks,1,1,"dummy2.csv")
    ev.evaluate()