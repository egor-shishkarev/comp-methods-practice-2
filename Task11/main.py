from examples import examples
from methods import gradient_projection, penalty_method, barrier_method
from utils import print_results
import numpy as np

print("Задача 11. Методы условной многомерной оптимизации")
print("""
Реализовать и сравнить методы по метрикам:
- скорость сходимости по числу вычислений оптимизируемой
  функции
- скорость сходимости по времени
- вероятность нахождения глобального оптимума
      
Список методов (выбрать три):
- МЕТОД ПРОЕКТИРОВАНИЯ ГРАДИЕНТА
- МЕТОД ШТРАФНЫХ ФУНКЦИЙ
- МЕТОД БАРЬЕРНЫХ ФУНКЦИЙ
- метод модифицированных функций Лагранжа
""")

for i in range(2):
    ex = examples[i]
    # x0 - начальное приближение, eq_cons - равенства с ограничениями, ineq_cons - неравенства с ограничениями
    print(f"Уравнение - {ex.func_str}")

    x_gp, f_gp, m_gp = gradient_projection(
        ex.func, ex.grad, ex.x0, ex.eq_cons, ex.ineq_cons,
    )
    print_results("Проектирование градиента", ex, x_gp, f_gp, m_gp)

    x_bar, f_bar, m_bar = barrier_method(
        ex.func, ex.grad, ex.x0,
        ex.ineq_cons,
    )
    print_results("Метод барьерных функций", ex, x_bar, f_bar, m_bar)

    if i == 1:
        ex.x0 = np.array([0.1, 0.1])
    x_pen, f_pen, m_pen = penalty_method(
        ex.func, ex.grad, ex.x0,
        ex.eq_cons, ex.ineq_cons,
    )
    print_results("Метод штрафных функций", ex, x_pen, f_pen, m_pen)

    input()
