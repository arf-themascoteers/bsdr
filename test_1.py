from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["pcal","lasso","mcuve","spa","bsnet","zhang","bsdr"],
        "datasets" : ["ghisaconus","indian_pines"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = Evaluator(tasks,1,10,"1.csv")
    ev.evaluate()