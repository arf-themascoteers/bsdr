from task_runner import TaskRunner

if __name__ == '__main__':
    tasks = {
        "algorithms" : ["bsdr1","bsdr2","bsdr3","bsdr4","bsdr"],
        "datasets" : ["ghisaconus","indian_pines","lucas"],
        "target_sizes" : [5, 10, 15, 20, 25, 30]
    }
    ev = TaskRunner(tasks,1,10,"bsdr.csv", skip_all_bands=True,verbose=True)
    ev.evaluate()
