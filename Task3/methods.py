import numpy

MAX_ITERATIONS = 700

def simple_iteration(A, b, epsilon):
    iterations = 0
    A = numpy.array(A)
    b = numpy.array(b)
    n = A.shape[0]

    B = numpy.zeros((n, n))
    c = numpy.zeros(n)

    for i in range(n):
        for j in range(n):
            if i == j:
                B[i][j] = 0
            else:
                B[i][j] = -A[i][j] / A[i][i]
        c[i] = b[i] / A[i][i]

    x = numpy.zeros(n)
    inaccuracy = numpy.linalg.norm(A @ x - b)

    while (inaccuracy > epsilon):
        x_new = numpy.dot(B, x) + c
        inaccuracy = numpy.linalg.norm(A @ x - b)
        x = x_new
        iterations += 1

        if (iterations > MAX_ITERATIONS):
            raise ValueError("Превышено максимальное количество итераций")

    return x, iterations
                
def seidel(A, b, epsilon):
    iterations = 0
    A = numpy.array(A)
    b = numpy.array(b)
    n = A.shape[0]

    x = numpy.zeros(n)
    x_new = numpy.zeros(n)
    inaccuracy = numpy.linalg.norm(A @ x - b)

    while (inaccuracy > epsilon):
        for i in range(n):
            sum1, sum2 = 0, 0
            for j in range(i):
                sum1 += A[i][j] * x_new[j]
            for j in range(i + 1, n):
                sum2 += A[i][j] * x[j]
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        inaccuracy = numpy.linalg.norm(A @ x - b)
        x = x_new.copy()
        iterations += 1
        
        if (iterations > MAX_ITERATIONS):
            raise ValueError("Превышено максимальное количество итераций")

    return x, iterations
        
    
    
