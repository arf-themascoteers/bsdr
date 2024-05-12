from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr"],
        "datasets" : ["indian_pines"],
        "target_sizes" : [5,10,15,20,25,30]
    }
    ev = TaskRunner(tasks,1,1,"bsdr.csv", skip_all_bands=True,verbose=False)
    ev.evaluate()
