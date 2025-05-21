# Реализовать два метода решения СЛАУ: «LU» и «QR»
# Проверить ответ
# Для матрицы А и матриц получившегося разложения вычислить числа обусловленности, сравнить их
# Протестировать на матрицах: хорошо обусловенных, [очень] плохо обусловенных
from methods import *
from utils import *
from matrices import *
import numpy

print('Задание 2. Точные методы решения СЛАУ')

# Создаем список пар (матрица, вектор правой части)
matrices = [
    (matrix_1, b_1),
    (matrix_2, b_2),
    (matrix_3, b_3)
]

for matrix, b in matrices:
    print("Матрица A:")
    print_matrix(matrix)
    
    L, U = LU(matrix)
    print("\nМатрица L:")
    print_matrix(L)
    print("\nМатрица U:")
    print_matrix(U)
    
    x = solve_LU(L, U, b)
    print("\nРешение x:")
    print(x)
    
    b_calc = matvec(matrix, x)
    print("\nПравая часть b:")
    print(b)
    print("\nВычисленная правая часть (Ax):")
    print(b_calc)
    
    error = numpy.linalg.norm(numpy.array(b) - b_calc)
    print(f"\nНорма отклонения: {error}")

    cond_A = numpy.linalg.cond(matrix)
    cond_L = numpy.linalg.cond(L)
    cond_U = numpy.linalg.cond(U)
    print(f"\nЧисло обусловленности матрицы A: {cond_A}")
    print(f"Число обусловленности матрицы L: {cond_L}")
    print(f"Число обусловленности матрицы U: {cond_U}")
    print("\n" + "="*50)
    input()
