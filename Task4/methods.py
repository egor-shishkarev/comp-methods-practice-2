import numpy

def accurate_method(A):
    A = numpy.array(A)
    eigvals, eigvecs = numpy.linalg.eig(A)
    idx = numpy.argmax(numpy.abs(eigvals))
    val = eigvals[idx].real
    vec = eigvecs[:, idx].real
    vec = vec / numpy.linalg.norm(vec)
    return vec, val

def power_method(A, epsilon, iteration_limit = 20000):
    A = numpy.array(A)
    n = A.shape[0]
    x_prev = numpy.ones(n) / n
    iteration = 0
    eigenvalue_prev = 0

    while iteration < iteration_limit:
        x_new = A @ x_prev
        eigenvalue_new = (x_new @ x_prev) / (x_prev @ x_prev)
        x_new = x_new / numpy.linalg.norm(x_new)

        if numpy.linalg.norm(eigenvalue_new - eigenvalue_prev) < epsilon:
            break

        x_prev = x_new
        eigenvalue_prev = eigenvalue_new
        iteration += 1

    return eigenvalue_new, x_prev, iteration


def scalar_product_method(A, epsilon, iteration_limit = 20000):
    A = numpy.array(A)
    n = A.shape[0]
    x_prev = numpy.ones(n) / n
    y_prev = numpy.ones(n) / n
    eigenvalue_prev = 0

    iteration = 0

    while iteration < iteration_limit:
        x_new = A @ x_prev
        y_new = A.T @ y_prev

        eigenvalue_new = (x_new @ y_new) / (x_prev @ y_new)

        x_new = x_new / numpy.linalg.norm(x_new)
        y_new = y_new / numpy.linalg.norm(y_new)

        if numpy.linalg.norm(eigenvalue_new - eigenvalue_prev) < epsilon:
            break

        x_prev, y_prev = x_new, y_new
        eigenvalue_prev = eigenvalue_new
        
        iteration += 1
    
    return eigenvalue_new, x_prev, iteration
