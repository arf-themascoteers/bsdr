from abc import ABC, abstractmethod
from data_splits import DataSplits
from metrics import Metrics
from datetime import datetime
from ds_manager import DSManager
from train_test_evaluator import evaluate_train_test_pair


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
        metric1, metric2 = evaluate_train_test_pair(task, evaluation_train_x, self.splits.evaluation_train_y, evaluation_test_x, self.splits.evaluation_test_y, self.splits.scaler)
        return metric1, metric2

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