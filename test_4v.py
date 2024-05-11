from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr"],
        "datasets" : ["ghisaconus","indian_pines","lucas"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = TaskRunner(tasks,1,1,"4v.csv", skip_all_bands=True,verbose=True)
    ev.evaluate()
