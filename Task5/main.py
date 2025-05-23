from matrices import *
from methods import *
from utils import *


print('Задача 5. Полная проблема собственных значений')

print("""
Реализовать метод Якоби поиска всех собственных чисел.
Использовать две какие-либо стратегии выбора обнуляемого элемента.
Сравнить.
- Вычисления проводить до достижения точности ε.
- Варьируя ε, изучить зависимость количества итераций от ε.
- Выводить количество итераций.
- По теореме Гершгорина определить область и её структуру, в
  которую должны попадать с.ч. матрицы. Проверить,
  действительно ли найденные значения в область попали.""")

matrices = [
    (matrix_1),
    (matrix_2),
    (matrix_3),
    (matrix_4),
]

epsilons = [1e-1, 1e-3, 1e-5]

for A in matrices:
    print("\nМатрица A:")
    print_matrix(A)
    eigenvalues_accurate, _ = numpy.linalg.eig(A)
    eigenvalues_accurate.sort()
    centers, radii = get_gershgorin_circles(A)
    for epsilon in epsilons:
        print(f"\n============ Точность: {epsilon} ============\n")
        print(f"Точные значения собственных чисел: - {eigenvalues_accurate}\n")

        try:
            eigenvalues_max_method, iterations = jacobi_method(A, epsilon)
            eigenvalues_max_method_sorted = sorted(eigenvalues_max_method.tolist())
            print("======= Наибольший недиагональный элемент =======\n")
            print_gershgorin_circles(centers, radii)
            print(f"Собственные значения: {eigenvalues_max_method_sorted}")
            print(f"Количество итераций: {iterations}")
            print(f"Погрешность: {eigenvalues_max_method_sorted - eigenvalues_accurate}\n")
        except ValueError:
            print(f"Превышено максимальное количество итераций - {MAX_ITERATIONS}\n")
        
        try:
            eigenvalues_opt_method, iterations = jacobi_method(A, epsilon, True)
            eigenvalues_opt_method_sorted = sorted(eigenvalues_opt_method.tolist())
            print("======= Стратегия оптимального элемента =======\n")
            print_gershgorin_circles(centers, radii)
            print(f"Собственные значения: {eigenvalues_opt_method_sorted}")
            print(f"Количество итераций: {iterations}")
            print(f"Погрешность: {eigenvalues_opt_method_sorted - eigenvalues_accurate}\n")
        except ValueError:
            print(f"Превышено максимальное количество итераций - {MAX_ITERATIONS}\n")
        input()
    
    print('=' + 50 * '=')
