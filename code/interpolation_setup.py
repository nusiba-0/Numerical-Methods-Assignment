import numpy as np
from scipy.interpolate import lagrange
from cubic_spline import cubic_spline_coeffs
from spline_eval import cubic_spline_eval


# --- Cubic spline evaluation function (moved here from spline_eval.py) ---
def cubic_spline_eval(x, y, M, xi):
    """
    Evaluate the cubic spline at a point xi.
    x, y : arrays of knots
    M    : array of second derivatives at knots
    xi   : point to evaluate
    """
    # Find the right interval for xi
    i = np.searchsorted(x, xi) - 1
    if i < 0:
        i = 0
    if i >= len(x) - 1:
        i = len(x) - 2

    h = x[i+1] - x[i]
    A = (x[i+1] - xi) / h
    B = (xi - x[i]) / h

    # Cubic spline formula
    Si = (A * y[i] + B * y[i+1] +
          ((A**3 - A) * M[i] + (B**3 - B) * M[i+1]) * (h**2) / 6.0)
    return Si
# Sample temperature data
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([15, 17, 20, 22, 21, 19, 16])

# Compute spline coefficients
M = cubic_spline_coeffs(x, y)

# Generate fine points
x_fine = np.linspace(x[0], x[-1], 200)

# Evaluate cubic spline
y_spline = np.array([cubic_spline_eval(x, y, M, xi) for xi in x_fine])

# Lagrange interpolation
poly_lagrange = lagrange(x, y)
y_lagrange = poly_lagrange(x_fine)
