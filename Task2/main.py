from methods import *
from utils import *
from matrices import *
import numpy

print('Задание 2. Точные методы решения СЛАУ\n')

matrices = [
    (matrix_1, b_1),
    (matrix_2, b_2),
    (matrix_3, b_3)
]

methods = [
    (LU, solve_LU, "LU"),
    (QR, solve_QR, "QR")
]

for matrix, b in matrices:
    for get_matrices, solve, name in methods:

        print("Матрица A:")
        print_matrix(matrix)
        
        print(f"\n============ {name} разложение ============")
        first_matrix, second_matrix = get_matrices(matrix)
        print(f"\nМатрица {name[0]}:")
        print_matrix(first_matrix)
        print(f"\nМатрица {name[1]}:")
        print_matrix(second_matrix)
        
        x = solve(first_matrix, second_matrix, b)
        print(f"\nРешение x ({name}):")
        print(x)
        
        b_calc = numpy.dot(matrix, x)
        print("\nПравая часть b:")
        print(b)
        print(f"\nВычисленная правая часть (Ax) для {name}:")
        print(b_calc)
        
        inaccuracy = numpy.linalg.norm(numpy.array(b) - b_calc)
        print(f"\nНорма отклонения для {name}: {inaccuracy}")
        
        cond_A = numpy.linalg.cond(matrix)
        cond_first_matrix = numpy.linalg.cond(first_matrix)
        cond_second_matrix = numpy.linalg.cond(second_matrix)
        print(f"\nЧисло обусловленности матрицы A: {cond_A}")
        print(f"Число обусловленности матрицы {name[0]}: {cond_first_matrix}")
        print(f"Число обусловленности матрицы {name[1]}: {cond_second_matrix}")
        input()
