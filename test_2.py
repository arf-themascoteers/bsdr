from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["pcal","lasso","mcuve","bsnet"],
        "datasets" : ["lucas"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = TaskRunner(tasks,1,10,"2.csv")
    ev.evaluate()