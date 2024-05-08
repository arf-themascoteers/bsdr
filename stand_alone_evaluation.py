from algorithm import Algorithm
from ds_manager import DSManager


def evaluate(dataset, folds, task, bands):
    r2s = []
    rmses = []
    d = DSManager(dataset,folds)
    for fold, splits in enumerate(d.get_k_folds()):
        evaluation_train_x = splits.evaluation_train_x[:,bands]
        evaluation_test_x = splits.evaluation_test_x[:,bands]
        r2, rmse = Algorithm.evaluate_train_test_pair(task, evaluation_train_x, splits.evaluation_train_y, evaluation_test_x, splits.evaluation_test_y)
        r2s.append(r2)
        rmses.append(rmse)
    print(bands,":",r2s)
    return r2s, rmses


def compare(dataset, folds, task, bands1, bands2):
    r2s1, rmses1 = evaluate(dataset, folds, task, bands1)
    r2s2, rmses2 = evaluate(dataset, folds, task, bands2)

    mean_r2s1 = sum(r2s1)/len(r2s1)
    mean_r2s2 = sum(r2s2)/len(r2s2)

    print(mean_r2s1)
    print(mean_r2s2)

    if mean_r2s1 > mean_r2s2:
        print(f"{bands1} is better than {bands2}")
    else:
        print(f"{bands2} is better than {bands1}")


dataset = "lucas"
folds = 10
task = "regression"
bands1 = [400,1000]
bands2 = [500,2000]

compare(dataset, folds, task, bands1, bands2)



