print("Задание 12. Метод Монте-Карло")

print("""
Задание: приближенно вычислять интеграл
- использовать функции, интеграл от которых известен
- попробовать функции, от которых взять интеграл непросто
      
Использовать 2 случайных величины, например, с постоянной
плотностью и с линейной плотностью, ведущей себя «похожим» на
g(x) образом, и несколько разных значения N.
Проводить сравнения. Посмотреть, дейтсвительно ли постоянная
плотность дает менее точные результаты.
      
Если есть возможность корректно генерировать двумерные рандомные
точки: реализовать «классическую» идею (что отношение площади
фигуры к площади прямоугольника будет примерно равно доле точек,
попавших внуть фигуры) и сранить результаты.

""")

from examples import *
from methods import *
from utils import *

integrals = [integral1, integral2, integral3, integral4]

for integral in integrals:
    print("="*60 + '\n')
    print('Подынтегральное выражение - ', integral.func_str)
    print(f"Границы интегрирования - [{integral.a}, {integral.b}]")
    lib_val, lib_err = accurate_value(integral)
    print(f"Точное (библиотечное значение): {lib_val:.9f} ± {lib_err:.2e}")

    for n in [1000, 5000, 20_000]:
        u, dots = monte_carlo_plain_area(integral, count=n)
        imp = monte_carlo_importance(integral, count=n)
        print(f"N = {n:>6}: постоянная плотность = {u:.9f}, линейная плотность = {imp:.9f}")
        print(f"Погрешность постоянной: {abs(lib_val - u)}, Погрешность линейной: {abs(lib_val - imp)}")
        visualize_integral(dots, integral)
        print()