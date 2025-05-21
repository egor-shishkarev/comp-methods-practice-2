from typing import List
import numpy

def LU(A: List[List[float]]):
    if (numpy.linalg.det(A) == 0):
        raise ValueError("Матрица вырожденная")
    A = numpy.array(A, dtype=float)
    n = A.shape[0]
    L = numpy.eye(n)
    U = A.copy()

    for k in range(n - 1):
        for i in range(k + 1, n):
            if abs(U[k, k]) < 1e-15:
                L[i, k] = 0.0
            else:
                L[i, k] = U[i, k] / U[k, k]
            for j in range(k, n):
                U[i, j] -= L[i, k] * U[k, j]

    return L, U

def solve_LU(L, U, b):
    #Ly = b
    y = numpy.zeros(len(b))
    for i in range(len(b)):
        sum = 0
        for j in range(i):
            sum += L[i][j] * y[j]
        y[i] = (b[i] - sum) / L[i][i]

    #Ux = y
    x = numpy.zeros(len(b))
    for i in range(len(b) - 1, -1, -1):
        sum = 0
        for j in range(i + 1, len(b)):
            sum += U[i][j] * x[j]
        x[i] = (y[i] - sum) / U[i][i]

    return x.tolist()

def QR(A: List[List[float]]):
    A = numpy.array(A, dtype=float)
    n, m = A.shape
    Q = numpy.eye(n)
    R = A.copy()

    for j in range(n):
        for i in range(m - 1, j, -1):
            a = R[j, j]
            b = R[i, j]
            r = numpy.sqrt(a**2 + b**2)
            c = a / r
            s = -b / r

            for k in range(j, n):
                t1 = R[j, k]
                t2 = R[i, k]
                R[j, k] = c * t1 - s * t2
                R[i, k] = s * t1 + c * t2

            for k in range(m):
                t1 = Q[k, j]
                t2 = Q[k, i]
                Q[k, j] = c * t1 - s * t2
                Q[k, i] = s * t1 + c * t2

    return Q, R

def solve_QR(Q, R, b):
    y = numpy.dot(Q.T, b)

    x = numpy.zeros(len(b))
    for i in range(len(b) - 1, -1, -1):
        sum = 0
        for j in range(i + 1, len(b)):
            sum += R[i][j] * x[j]
        x[i] = (y[i] - sum) / R[i][i]

    return x.tolist()