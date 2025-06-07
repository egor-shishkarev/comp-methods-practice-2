import math
from math import sin, exp

from methods import solve_bvp
from utils import ConsoleHelper, plot_error, plot_solution

class BoundaryValueProblem:
    """
    Класс, представляющий краевую задачу вида:
    -p(x)u'' + q(x)*u' + r(x)*u = f(x)

    с граничными условиями:
    alpha_1*u(a) - alpha_2*u'(a) = alpha
    beta_1*u(b) + beta_2*u'(b) = beta
    """

    def __init__(self, p_func, q_func, r_func, f_func, a, b,
                    alpha_1, alpha_2, alpha, beta_1, beta_2, beta):
        self.p_func = p_func
        self.q_func = q_func
        self.r_func = r_func
        self.f_func = f_func
        self.a = a
        self.b = b
        self.alpha_1 = alpha_1
        self.alpha_2 = alpha_2
        self.alpha = alpha
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.beta = beta

    def __str__(self):
        """Строковое представление задачи для вывода"""
        equation_str = f"-p(x)u'' + q(x)u' + r(x)u = f(x)"
        boundary_str = f"u({self.a}) = {self.alpha}, "
        if self.beta_2 == 0:
            boundary_str += f"u({self.b}) = {self.beta}"
        else:
            boundary_str += f"u({self.b}) + {self.beta_2}u'({self.b}) = {self.beta}"
        return f"Дифференциальное уравнение:\n{equation_str}\nГраничные условия:\n{boundary_str}" 

def main():
    """Основная функция для настройки и решения задачи"""

    # ======== Задача 1 (исходная) ========
    def p_func1(x):
        return -(x - 2) / (x + 2)

    def q_func1(x):
        return x

    def r_func1(x):
        return 1 - sin(x)

    def f_func1(x):
        return x ** 2

    # Область и граничные условия
    a1 = -1
    b1 = 1
    alpha1 = 0
    beta1 = 0
    alpha_1_1 = 1
    alpha_2_1 = 0
    beta_1_1 = 1
    beta_2_1 = 2

    # Создаем экземпляр задачи
    problem1 = BoundaryValueProblem(
        p_func1, q_func1, r_func1, f_func1,
        a1, b1, alpha_1_1, alpha_2_1, alpha1, beta_1_1, beta_2_1, beta1
    )

    # ======== Задача 2 ========
    def p_func2(x):
        return 1.0 / (x - 3.0)

    def q_func2(x):
        return 1.0 + x / 2.0

    def r_func2(x):
        return -exp(x / 2.0)

    def f_func2(x):
        return 2.0 - x

    a2 = -1.0
    b2 = 1.0
    alpha2 = 0.0
    beta2 = 0.0
    alpha_1_2 = -1.0
    alpha_2_2 = 0.0
    beta_1_2 = 1.0
    beta_2_2 = 0.0

    problem2 = BoundaryValueProblem(
        p_func2, q_func2, r_func2, f_func2,
        a2, b2, alpha_1_2, alpha_2_2, alpha2, beta_1_2, beta_2_2, beta2
    )

    # ======== Задача 3 ========
    def p_func3(x):
        return -1

    def q_func3(x):
        return 0

    def r_func3(x):
        return x**2

    def f_func3(x):
        return (math.pi**2/4+x**2)*math.cos(math.pi*x/2)

    a3 = -1.0
    b3 = 1.0
    alpha3 = 0.0
    beta3 = 0.0
    alpha_1_3 = 1.0
    alpha_2_3 = 0.0
    beta_1_3 = 1.0
    beta_2_3 = 0.0

    problem3 = BoundaryValueProblem(
        p_func3, q_func3, r_func3, f_func3,
        a3, b3, alpha_1_3, alpha_2_3, alpha3, beta_1_3, beta_2_3, beta3
    )

    print("Реализовать решение ОДУ сеточным методом")
    print("- Начинаться вычисления с грубой сетки; измельчаться сетку и уточнять по Ричардсону")
    print("- Выводить полученное приближение. Можно на картинке.")

    # Решаем задачи и выводим результаты
    print("=" * 50)
    print("РЕШЕНИЕ ИСХОДНОЙ ЗАДАЧИ")
    print("(-(x - 2) / (x + 2)) * u_xx + x * u_x - (1 - sin(x)) * u = x ** 2 ")
    print("Интервал: (-1, 1)")
    print("Граничные условия: u(-1) = 0 | u(1) + 2u'(1) = 0")
    print("=" * 50)
    x_values1, u_values1, errors1, n1 = solve_bvp(problem1)
    result1 = ConsoleHelper(x_values1, u_values1, errors1, n1)
    print(result1)
    plot_error(errors1, "\n(-(x - 2) / (x + 2)) * u_xx + x * u_x - (1 - sin(x)) * u = x ** 2 ")
    plot_solution(x_values1, u_values1, "\nu(-1) = 0 | u(1) + 2u'(1) = 0")

    print("\n" + "=" * 50)
    print("РЕШЕНИЕ НОВОЙ ЗАДАЧИ 2")
    print("(1 / (x - 3)) * u_xx + (1 + x/2) * u_x - (-exp(x/2)) * u = 2 - x ")
    print("Интервал: (-1, 1)")
    print("Граничные условия: -u(-1) = 0 | u(1) = 0")
    print("=" * 50)
    x_values2, u_values2, errors2, n2 = solve_bvp(problem2)
    result2 = ConsoleHelper(x_values2, u_values2, errors2, n2)
    print(result2)
    plot_error(errors2, "\n(1 / (x - 3)) * u_xx + (1 + x/2) * u_x - (-exp(x/2)) * u = 2 - x")
    plot_solution(x_values2, u_values2, "\nu(-1) = 0 | u(1) = 0")

    print("\n" + "=" * 50)
    print("РЕШЕНИЕ НОВОЙ ЗАДАЧИ 3")
    print("-u_xx - (x^2) * u = (π*2/4 + x^2) * cos(π * x/2)")
    print("Интервал: (-1, 1)")
    print("Граничные условия: u(-1) = 0 | u(1) = 0")
    print("=" * 50)
    x_values3, u_values3, errors3, n3 = solve_bvp(problem3)
    result3 = ConsoleHelper(x_values3, u_values3, errors3, n3)
    print(result3)
    plot_error(errors3, "\n-u_xx - (x^2) * u = (π*2/4 + x^2) * cos(π * x/2)")
    plot_solution(x_values3, u_values3, "\nu(-1) = 0 | u(1) = 0")

if __name__ == '__main__':
    main()
