import numpy as np
from scipy.interpolate import lagrange
from cubic_spline import cubic_spline_coeffs
from spline_eval import cubic_spline_eval

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
