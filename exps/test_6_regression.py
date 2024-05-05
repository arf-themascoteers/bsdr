from evaluator import Evaluator

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr","bsnet","mcuve","pcal","lasso"],
        "datasets" : ["lucas_skipped","lucas_downsampled","lucas_min"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = Evaluator(tasks,1,10,"test_6_regression.csv")
    ev.evaluate()