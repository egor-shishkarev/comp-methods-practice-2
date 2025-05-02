import numpy as np
from scipy.linalg import hilbert, solve, inv
from methods import *
from utils import *

n = 5

hilbert_matrix = hilbert(n)

random_matrix = create_random_matrix(n)

tridiagonal_matrix_1 = [
    [1, 2, 0, 0, 0],
    [2, 3, 4, 0, 0],
    [0, 4, 5, 6, 0],
    [0, 0, 6, 7, 8],
    [0, 0, 0, 8, 9],
]

tridiagonal_matrix_2 = [
    [25, -13, 0, 0, 0],
    [-27, 48, 5, 0, 0],
    [0, 7, 103, -67, 0],
    [0, 0, -9, 17, 1],
    [0, 0, 0, -1, 5],
]

diagonal_matrix = [
    [1, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 3, 0, 0],
    [0, 0, 0, 4, 0],
    [0, 0, 0, 0, 5],
]

b = np.ones(n)
b_tilde = b + 1e-2 * np.random.randn(n)

matrices = [random_matrix, hilbert_matrix, diagonal_matrix, tridiagonal_matrix_1, tridiagonal_matrix_2]
matrices_names = ['Случайная матрица', 'Матрица Гильберта', 'Диагональная матрица', 'Трехдиагональная матрица', 'Трехдиагональная матрица с диагональным преобладанием']

for index, matrix in enumerate(matrices):
    A = np.array(matrix)
    np.set_printoptions(precision=2, suppress=True)
    print(matrices_names[index], ':\n', sep='')
    solution = solve(A, b)
    print_system(A, solution, b)
    print('\nПроизводим возмущение системы: \n')
    solution_tilde = solve(A, b_tilde)
    print_system(A, solution_tilde, b_tilde)  
    cond_spectral = get_spectral_condition_number(A)
    cond_volume = get_volume_condition_number(A)
    cond_angle = get_angular_condition_number(A)
    print('\nНорма разности между начальным и возмущенным решением: ', norm(solution - solution_tilde))
    print(f"Спектральное число обусловленности: {cond_spectral:.6e}")
    print(f"Объёмное число обусловленности:    {cond_volume:.6e}")
    print(f"Угловое число обусловленности:     {cond_angle:.6e}")
    print()