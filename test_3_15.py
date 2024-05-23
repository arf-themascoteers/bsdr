from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["spa"],
        "datasets" : ["lucas"],
        "target_sizes" : [15]
    }
    ev = TaskRunner(tasks,1,1,"3_15.csv")
    ev.evaluate()