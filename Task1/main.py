import numpy as np
from scipy.linalg import hilbert, solve
from methods import *
from utils import *
from matrices import *

print('Задание 1. Числа обусловленности')
print("""
Для СЛАУ с некоторой матрицей A:
- вычислить числа обусловленности;
- поварьировав матрицу и/или правую часть, вычислить |x − x˜|;
- посмотреть, есть ли зависимость между величинами чисел обусловленности и погрешностью решения.
""")

N = 5

hilbert_matrix = hilbert(N)

random_matrix = create_random_matrix(N)

b = np.ones(N)
b_tilde = b + 1e-2 * np.random.randn(N)

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
    input()