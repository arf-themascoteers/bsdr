from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr"],
        "datasets" : ["indian_pines"],
        "target_sizes" : [25, 30]
    }
    ev = TaskRunner(tasks,1,10,"101.csv")
    ev.evaluate()