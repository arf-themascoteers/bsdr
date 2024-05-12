from algorithm import Algorithm
from ds_manager import DSManager
from train_test_evaluator import evaluate_train_test_pair


def evaluate(dataset, folds, task, bands):
    r2s = []
    rmses = []
    d = DSManager(dataset,folds)
    for fold, splits in enumerate(d.get_k_folds()):
        evaluation_train_x = splits.evaluation_train_x[:,bands]
        evaluation_test_x = splits.evaluation_test_x[:,bands]

        r2, rmse = evaluate_train_test_pair(task, evaluation_train_x, splits.evaluation_train_y, evaluation_test_x, splits.evaluation_test_y, splits.scaler)
        r2s.append(r2)
        rmses.append(rmse)
    return r2s, rmses


def compare(dataset, folds, task, bands1, bands2):
    r2s1, rmses1 = evaluate(dataset, folds, task, bands1)
    r2s2, rmses2 = evaluate(dataset, folds, task, bands2)

    mean_r2s1 = sum(r2s1)/len(r2s1)
    mean_r2s2 = sum(r2s2)/len(r2s2)

    if mean_r2s1 > mean_r2s2:
        print(f"First is better")
    else:
        print(f"Second is better")

    print(r2s1, rmses1)
    print(r2s2, rmses2)

    mean_rm1 = sum(rmses1)/len(rmses1)
    mean_rm2 = sum(rmses2)/len(rmses2)

    print(mean_r2s1, mean_r2s2)
    print(mean_rm1, mean_rm2)

dataset = "indian_pines"
folds = 10
task = "classification"
bands1 = [10,16,24,27,40,47,53,59,63,78,83,92,100,106,119,120,129,140,145,153,154,166,176,182,190]
bands2 = [165,38,51,65,12,100,0,71,5,60,88,26,164,75,74,52,22,94,35,11,184,179,34,160,46]

compare(dataset, folds, task, bands1, bands2)



