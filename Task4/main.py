from matrices import *
from methods import *
from utils import *

print('Задание 4. Частичная проблема собственных значений\n')

print("""
Реализовать для нахождения максимального по модулю собственного
числа и соответствующего собственного вектора матрицы степенной
метод и метод скалярных произведений.
- Вычисления проводить до достижения точности ε.
- Варьируя ε, изучить зависимость количества итераций от ε.
- Сравнить количество итераций в методах (при каждом
  фиксированном ε), если такое сравнение корректно.
""")

matrices = [
    (matrix_1),
    (matrix_2),
    (matrix_3),
    (matrix_4)
]

epsilons = [1e-3, 1e-6, 1e-9]

for A in matrices:
    print("\nМатрица A:")
    print_matrix(A)

    accurate_eigenvector, accurate_eigenvalue = accurate_method(A)

    for epsilon in epsilons:
        print(f"\n============ Точность: {epsilon} ============\n")
        print(f"Точное значение наибольшего по модулю собственного числа: - {accurate_eigenvalue}")
        print(f"Собственный вектор, соответствующий этому числу: {accurate_eigenvector.tolist()}\n")
        try:
            eigenvalue, eigenvector, iterations = power_method(A, epsilon)
            print("======= Степенной метод =======\n")
            print(f"Собственное значение: {eigenvalue}")
            print(f"Собственный вектор: {eigenvector}")
            print(f"Количество итераций: {iterations}\n")
        except ValueError:
            print("Для данной матрицы и точности степенной метод не сходится\n")
        
        try:
            eigenvalue, eigenvector, iterations = scalar_product_method(A, epsilon)
            print("======= Метод скалярных произведений =======\n")
            print(f"Собственное значение: {eigenvalue}")
            print(f"Собственный вектор: {eigenvector}")
            print(f"Количество итераций: {iterations}\n")
        except ValueError:
            print("Для данной матрицы и точности метод скалярных произведений не сходится\n")
        input()
    
    print('=' + 50 * '=')
        