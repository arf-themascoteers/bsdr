from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr11","bsdr5"],
        "datasets" : ["indian_pines","lucas", "ghisaconus"],
        "target_sizes" : [25,10, 15, 20,30, 5]
    }
    ev = TaskRunner(tasks,1,10,"bsdr.csv", skip_all_bands=True,verbose=True)
    ev.evaluate()
