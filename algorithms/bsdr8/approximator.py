import torch
from torchcubicspline import(natural_cubic_spline_coeffs, NaturalCubicSpline)


def get_splines(X, device=None):
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    X = X.permute(1, 0)
    indices = torch.linspace(0, 1, X.shape[0]).to(device)
    coeffs = natural_cubic_spline_coeffs(indices, X)
    spline = NaturalCubicSpline(coeffs)
    return spline

