from matrices import *
from methods import *
from utils import *

print('Задание 3. Итерационные методы решения СЛАУ')

print("""
- Реализовать решение СЛАУ двумя итерационными методами:
  методом простой итерации + методом Зейделя.
- Сравнить количество итераций, если это сравнение корректно.
- Находить решения с разной точностью.
- Протестировать работу методов на симметричных с
  диагональным преобладанием разреженных матрицах большого
  порядка (больше 1000).
""")

matrices = [
    (matrix_1, b_1),
    (matrix_2, b_2),
    (matrix_3, b_3),
    (matrix_4, b_4),
]

epsilons = [1e-3, 1e-6, 1e-9]

for A, b in matrices:
    if (hasattr(A, 'shape') and A.shape[0] > 1000):
        print('Матрица A: симметричная, разреженная, с диагональным преобладанием\n')
        A = A.toarray()
        print("Матрица A: \n", A)
        print("\nПравая часть b: \n", b, "\n")
    else:
        print("Матрица A:")
        print_matrix(A)

        print("\nПравая часть b:")
        print(b, '\n')

    accurate_solution = numpy.linalg.solve(A, b)

    for epsilon in epsilons:
        print(f"============ Точность: {epsilon} ============\n")
        print(f"Точное решение - {accurate_solution}\n")
        try:
            x, iterations = simple_iteration(A, b, epsilon)
            print(f"Решение методом простой итерации: {x}")
            print(f"Количество итераций: {iterations}\n")
        except ValueError:
            print("Для данной матрицы и точности метод простой итерации не сходится\n")
        
        try:
            x, iterations = seidel(A, b, epsilon)
            print(f"Решение методом Зейделя: {x}")
            print(f"Количество итераций: {iterations}\n")
        except ValueError:
            print("Для данной матрицы и точности метод Зейделя не сходится\n")
    print('=' + 50 * '=')
    input()
