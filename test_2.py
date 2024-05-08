from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["pcal","lasso","mcuve","bsnet","bsdr"],
        "datasets" : ["lucas"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = Evaluator(tasks,1,10,"2.csv")
    ev.evaluate()