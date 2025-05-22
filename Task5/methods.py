import numpy
import math

MAX_ITERATIONS = 1000

def jacobi_method(A, epsilon, is_optimal=False):
    A = numpy.array(A, dtype=float)
    A = A.copy()
    iterations = 0

    method = get_optimal_element if is_optimal else get_max_off_diagonal

    while (not is_all_gergoshin_radiuses_fit(A, epsilon)):
        i, j = method(A)

        R = get_rotation_matrix(A, i, j)
        A = R.T @ A @ R
        iterations += 1

        if (iterations > MAX_ITERATIONS):
            raise ValueError("Превышено максимальное количество итераций")

    return A.diagonal(), iterations

def get_max_off_diagonal(A):
    A = numpy.array(A, dtype=float)
    n = A.shape[0]
    max_i, max_j = -1, -1
    max_element = -math.inf

    for i in range(n):
        for j in range(i + 1, n):
            if (i == j):
                continue
            else:
                if (abs(A[i][j])) > max_element:
                    max_element = abs(A[i][j])
                    max_i = i
                    max_j = j
    
    return max_i, max_j

def get_optimal_element(A):
    max_radius = -1
    index_of_max_radius = -1

    for i in range(A.shape[0]):
        radius = get_gershgorin_radius(A, i)
        if (radius > max_radius):
            max_radius = radius
            index_of_max_radius = i

    max_element = -1
    index_of_max_element = -1

    for i in range(A.shape[1]):
        if (i == index_of_max_radius):
            continue
        element = abs(A[index_of_max_radius][i])
        if (element > max_element):
            max_element = element
            index_of_max_element = i

    return index_of_max_radius, index_of_max_element

def get_rotation_matrix(A, i, j):
    A = numpy.array(A)
    if (i > j):
        i, j = j, i
    n = A.shape[0]
    R = numpy.identity(n)

    if (abs(A[i][j]) < 1e-16):
        return numpy.identity(n)

    if (abs(A[i][i] - A[j][j])) < 1e-16:
        phi = math.pi / 4
    else:
        phi = 0.5 * math.atan2(2*A[i][j], (A[i][i] - A[j][j]))

    c = math.cos(phi)
    s = math.sin(phi)
    
    R[i][i] = c
    R[i][j] = -s
    R[j][i] = s
    R[j][j] = c

    return R

def get_gershgorin_radius(A, i):
    sum = 0
    for j in range(A.shape[1]):
        if (i != j):
            sum += abs(A[i][j])
    return sum


def is_all_gergoshin_radiuses_fit(A, epsilon):
    A = numpy.array(A)
    n = A.shape[0]

    for i in range(n):
        if (get_gershgorin_radius(A, i) >= epsilon):
            return False
    
    return True

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0