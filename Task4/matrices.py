from utils import create_random_matrix
from scipy.linalg import hilbert

matrix_1 = [
    [4, 1, 0],
    [1, 4, 1],
    [0, 1, 4],
]

matrix_2 = [
    [8, 3, 1, -2],
    [3, 7, 2, 1],
    [1, 2, 10, -3],
    [2, -1, 3, 8]
]

matrix_3 = hilbert(5)

matrix_4 = create_random_matrix(7)
