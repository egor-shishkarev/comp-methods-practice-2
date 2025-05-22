from scipy.linalg import hilbert

matrix_1 = [
    [4, 1, 0],
    [1, 4, 1],
    [0, 1, 4],
]

matrix_2 = [
    [-5, 7,  11, 22],
    [ 7, 9,   8, 13],
    [11, 8, -25,  0],
    [22, 13,  0, 59],
]

matrix_3 = hilbert(5)

matrix_4 = hilbert(7)