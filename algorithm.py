from abc import ABC, abstractmethod
from data_splits import DataSplits
from metrics import Metrics
from datetime import datetime
from sklearn.svm import SVR
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from ds_manager import DSManager
from sklearn.metrics import r2_score, mean_squared_error
import math
from sklearn.metrics import accuracy_score
from sklearn.metrics import cohen_kappa_score


class Algorithm(ABC):
    def __init__(self, target_size:int, splits:DataSplits, repeat=0, fold=0):
        self.target_size = target_size
        self.splits = splits
        self.repeat = repeat
        self.fold = fold
        self.selected_indices = []
        self.model = None
        self.all_indices = None

    def fit(self):
        self.model, self.selected_indices = self.get_selected_indices()
        return self.selected_indices

    def transform(self, X):
        if len(self.selected_indices) != 0:
            return self.transform_with_selected_indices(X, self.selected_indices)
        return self.model.transform(X)

    @staticmethod
    def transform_with_selected_indices(X, selected_indices):
        return X[:,selected_indices]

    def compute_performance(self):
        start_time = datetime.now()
        selected_features = self.fit()
        elapsed_time = (datetime.now() - start_time).total_seconds()
        evaluation_train_x = self.transform(self.splits.evaluation_train_x)
        evaluation_test_x = self.transform(self.splits.evaluation_test_x)
        metric1, metric2 = self.compute_performance_with_transformed_xs(evaluation_train_x, evaluation_test_x)
        return Metrics(elapsed_time, metric1, metric2, selected_features)

    def compute_performance_with_selected_indices(self, selected_indices):
        evaluation_train_x = Algorithm.transform_with_selected_indices(self.splits.evaluation_train_x, selected_indices)
        evaluation_test_x = Algorithm.transform_with_selected_indices(self.splits.evaluation_test_x, selected_indices)
        return self.compute_performance_with_transformed_xs(evaluation_train_x, evaluation_test_x)

    def compute_performance_with_transformed_xs(self, evaluation_train_x, evaluation_test_x):
        task = DSManager.get_task_by_dataset_name(self.splits.get_name())
        metric1, metric2 = Algorithm.evaluate_train_test_pair(task,
                                                              evaluation_train_x, self.splits.evaluation_train_y,
                                                              evaluation_test_x, self.splits.evaluation_test_y)
        return metric1, metric2

    @staticmethod
    def evaluate_train_test_pair(task, X_train, y_train, X_test, y_test):
        evaluator_algorithm = Algorithm.get_metric_evaluator(task)
        evaluator_algorithm.fit(X_train, y_train)
        y_pred = evaluator_algorithm.predict(X_test)
        return Algorithm.calculate_metrics(task, y_test, y_pred)

    @staticmethod
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

    @staticmethod
    def calculate_metrics(task, y_test, y_pred):
        if task == "classification":
            return Algorithm.calculate_metrics_for_classification(y_test, y_pred)
        return Algorithm.calculate_metrics_for_regression(y_test, y_pred)

    @staticmethod
    def calculate_metrics_for_classification(y_test, y_pred):
        accuracy = accuracy_score(y_test, y_pred)
        kappa = cohen_kappa_score(y_test, y_pred)
        return accuracy, kappa

    @staticmethod
    def calculate_metrics_for_regression(y_test, y_pred):
        r2 = r2_score(y_test, y_pred)
        rmse = math.sqrt(mean_squared_error(y_test, y_pred))
        return r2, rmse

    @abstractmethod
    def get_selected_indices(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    def get_all_indices(self):
        return self.all_indices

    def _set_all_indices(self, all_indices):
        self.all_indices = all_indices

    def is_independent_of_target_size(self):
        name = self.get_name()
        for ind in ["lasso","bsnet","logistic", "pca", "zhang"]:
            if name in ind:
                return True
        return False