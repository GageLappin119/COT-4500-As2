import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, interp1d


def Nevilles_Method(x, y, w):
    n = len(x)
    neville = np.zeros((n, n))

    for i in range(n):
        neville[i][0] = y[i]

    for i in range(1, n):
        for j in range(1, i + 1):
            neville[i][j] = ((w - x[i - j]) * neville[i][j - 1] - (w - x[i]) * neville[i - 1][j - 1]) / (x[i] - x[i - j])

    return neville[n - 1][n - 1]  # Return the interpolated value


def Newton_Forward(xi, fxi, w):
    lim = len(xi)
    diffs = np.zeros((lim, lim))

    for i in range(lim):
        diffs[i][0] = fxi[i]

    for i in range(1, lim):
        for j in range(i, lim):
            diffs[j][i] = (diffs[j][i - 1] - diffs[j - 1][i - 1]) / (xi[j] - xi[j - i])

    # Compute interpolation value using forward formula
    result = fxi[0]
    term = 1
    for i in range(1, lim):
        term *= (w - xi[i - 1])
        result += term * diffs[i][i]

    return result


def Divided_Difference(x_values, f_values, f_derivatives):
    # Initialize the divided difference table with zeros
    n = len(x_values)
    divided_diff = np.zeros((n, n))

    # First column is f(x)
    divided_diff[:, 0] = f_values

    # First divided differences (derivatives for repeated points)
    for i in range(1, n, 2):
        divided_diff[i, 1] = f_derivatives[i]  # f'(x) for repeated x-values
        if i+1 < n:
            divided_diff[i+1, 1] = (divided_diff[i+1, 0] - divided_diff[i, 0]) / (x_values[i+1] - x_values[i])

    # Higher-order divided differences
    for j in range(2, n):  # Column
        for i in range(n - j):  # Row
            divided_diff[i, j] = (divided_diff[i+1, j-1] - divided_diff[i, j-1]) / (x_values[i+j] - x_values[i])

    # Print results
    return divided_diff



def Cubic_Spline(x, y):
    # Create a cubic spline interpolator
    h = np.zeros(len(x) - 1)
    b = np.zeros(len(x))

    for i in range(len(x) - 1):
        h[i] = x[i + 1] - x[i]

    for i in range(len(x)):
        if i == 0:
            b[i] = 0
        elif i == len(x) - 1:
            b[i] = 0
        else:
            b[i] = ((3 / h[i]) * (y[i + 1] - y[i])) - (3 / h[i - 1]) * (y[i] - y[i - 1])

    
    print(b)

    return h
