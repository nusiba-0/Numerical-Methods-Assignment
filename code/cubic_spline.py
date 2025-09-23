import numpy as np

def cubic_spline_coeffs(x, y):
    n = len(x) - 1
    h = np.diff(x)

   
    A = np.zeros((n-1, n-1))
    B = np.zeros(n-1)

    for i in range(1, n):
        if i != 1:
            A[i-1, i-2] = h[i-1] / 6
        A[i-1, i-1] = (h[i-1] + h[i]) / 3
        if i != n-1:
            A[i-1, i] = h[i] / 6

        B[i-1] = (y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1]

    M = np.linalg.solve(A, B)
    M = np.concatenate(([0], M, [0]))
    return M
