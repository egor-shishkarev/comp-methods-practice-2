from utils import generate_tridiag_spd
import numpy

matrix_1 = [
    [4, 1, 0],
    [1, 4, 1],
    [0, 1, 4],
]
b_1 = [1, 2, 3]

matrix_2 = [
    [1, 0.99],
    [0.99, 0.98]
]

b_2 = [1.99, 1.97]


matrix_3 = [
    [8, 3, 1, -2],
    [3, 7, 2, 1],
    [1, 2, 10, -3],
    [2, -1, 3, 8]
]
b_3 = [1, 1, 1, 1]

matrix_4 = generate_tridiag_spd(1500)

b_4 = numpy.ones(1500)