from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr"],
        "datasets" : ["ghisaconus"],
        "target_sizes" : [10]
    }
    ev = TaskRunner(tasks,1,10,"g10.csv", skip_all_bands=True,verbose=True)
    ev.evaluate()
