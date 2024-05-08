from sklearn.metrics import mean_squared_error, r2_score
import math


def calculate_r2(y, y_hat, scaler):
    y = scaler.inverse_transform(y)
    y_hat = scaler.inverse_transform(y_hat)
    r2 = r2_score(y, y_hat)
    return r2


def calculate_rmse(y, y_hat, scaler):
    y = scaler.inverse_transform(y)
    y_hat = scaler.inverse_transform(y_hat)
    rmse = math.sqrt(mean_squared_error(y, y_hat))
    return rmse