from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["spa"],
        "datasets" : ["lucas"],
        "target_sizes" : [5, 10]
    }
    ev = TaskRunner(tasks,1,1,"3_5_10.csv")
    ev.evaluate()