from sklearn.metrics import accuracy_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import math


def calculate_r2(y, y_hat, scaler):
    y = scaler.inverse_transform(y.reshape(-1, 1)).reshape(-1)
    y_hat = scaler.inverse_transform(y_hat.reshape(-1, 1)).reshape(-1)
    r2 = r2_score(y, y_hat)
    return r2


def calculate_rmse(y, y_hat, scaler):
    y = scaler.inverse_transform(y.reshape(-1, 1)).reshape(-1)
    y_hat = scaler.inverse_transform(y_hat.reshape(-1, 1)).reshape(-1)
    rmse = math.sqrt(mean_squared_error(y, y_hat))
    return rmse