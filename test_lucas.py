from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr"],
        "datasets" : ["lucas"],
        "target_sizes" : [5]
    }
    ev = TaskRunner(tasks,1,10,"luc_all.csv")
    ev.evaluate()