from sklearn.svm import SVR
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
import calculator


def evaluate_train_test_pair(task, evaluation_train_x, evaluation_train_y, evaluation_test_x, evaluation_test_y, scaler):
    evaluator_algorithm = get_metric_evaluator(task)
    evaluator_algorithm.fit(evaluation_train_x, evaluation_train_y)
    y_pred = evaluator_algorithm.predict(evaluation_test_x)
    return calculate_metrics(task, evaluation_test_y, y_pred, scaler)


def calculate_metrics(task, y_test, y_pred, scaler):
    if task == "classification":
        return calculate_metrics_for_classification(y_test, y_pred)
    return calculate_metrics_for_regression(y_test, y_pred, scaler)


def calculate_metrics_for_classification(y_test, y_pred):
    accuracy = calculator.accuracy_score(y_test, y_pred)
    kappa = calculator.cohen_kappa_score(y_test, y_pred)
    return accuracy, kappa


def calculate_metrics_for_regression(y_test, y_pred, scaler):
    r2 = calculator.calculate_r2(y_test, y_pred, scaler)
    rmse = calculator.calculate_rmse(y_test, y_pred, scaler)
    return r2, rmse


def get_metric_evaluator(task):
    gowith = "sv"

    if gowith == "rf":
        if task == "regression":
            return RandomForestRegressor()
        return RandomForestClassifier()
    elif gowith == "sv":
        if task == "regression":
            return SVR(C=100, kernel='rbf', gamma=1.)
        return SVC(C=1e5, kernel='rbf', gamma=1.)
    else:
        if task == "regression":
            return MLPRegressor(max_iter=2000)
        return MLPClassifier(max_iter=2000)