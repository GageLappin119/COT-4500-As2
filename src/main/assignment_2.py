import numpy as np

def Nevilles_Method(x, y, w):
    n = len(x)
    neville = np.zeros((n, n))

    for i in range(n):
        neville[i][0] = y[i]

    for i in range(1, n):
        for j in range(1, i + 1):
            neville[i][j] = ((w - x[i - j]) * neville[i][j - 1] - (w - x[i]) * neville[i - 1][j - 1]) / (x[i] - x[i - j])

    return neville[n - 1][n - 1] # Return the interpolated value


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
    
    return (result, diffs[1, 1], diffs[2, 2], diffs[3, 3])

def Divided_Difference(x_values, f_values, f_derivatives):
    # Initialize the divided difference table with zeros
    n = len(x_values)
    divided_diff = np.zeros((n, n - 1))

    # First column is x
    divided_diff[:, 0] = x_values

    # Second column is f(x)
    divided_diff[:, 1] = f_values

    # First divided differences (handling repeated x-values)
    for i in range(n):
        if i % 2 == 1:  # Every second point is a repeated x-value
            divided_diff[i, 2] = f_derivatives[i]  # Use derivative for repeated values
        elif i > 0:
            divided_diff[i, 2] = (divided_diff[i, 1] - divided_diff[i - 1, 1]) / (x_values[i] - x_values[i - 1])

    # Compute higher-order divided differences
    for j in range(3, n - 1):
        for i in range(j - 1, n):
            divided_diff[i, j] = (divided_diff[i, j - 1] - divided_diff[i - 1, j - 1]) / (x_values[i] - x_values[i - (j - 1)])

    np.set_printoptions(precision=8, suppress=False,linewidth=200)
     
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

    a = np.zeros((len(x), len(x)))
    a[0,0] = 1
    a[len(x) - 1, len(x) - 1] = 1

    for i in range(1, len(x) - 1):
        a[i, i - 1] = h[i - 1]
        a[i, i ] = 2*(h[i - 1] + h[i])
        a[i, i + 1] = h[i]
    np.set_printoptions()

    x = np.array(np.linalg.solve(a, b))

    return (a, b, x) 
