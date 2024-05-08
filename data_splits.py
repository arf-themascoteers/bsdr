class DataSplits:
    def __init__(self,
                 name,
                 scaler,
                 train_x, train_y,
                 validation_x, validation_y,
                 evaluation_train_x, evaluation_train_y,
                 evaluation_test_x, evaluation_test_y):
        self.name = name
        self.scaler = scaler
        self.train_x = train_x
        self.train_y = train_y
        self.validation_x = validation_x
        self.validation_y = validation_y
        self.evaluation_train_x = evaluation_train_x
        self.evaluation_train_y = evaluation_train_y
        self.evaluation_test_x = evaluation_test_x
        self.evaluation_test_y = evaluation_test_y

    def get_name(self):
        return self.name

    def print_splits(self):
        print(f"train={len(self.train_y)}; valid={len(self.validation_y)}; "
              f"evaluation_train={len(self.evaluation_train_y)}; evaluation_test={len(self.evaluation_test_y)};")