print("Задание 10. Методы безусловной многомерной оптимизации")

print("""
Реализовать и сравнить методы по метрикам:
- скорость сходимости по числу вычислений оптимизируемой
  функции
- скорость сходимости по времени
- точность метода
- вероятность нахождения глобального оптимума
      
Список методов первого порядка (выбрать три):
- ГРАДИЕНТНЫЙ СПУСК
- наискорейший спуск
- МЕТОД ТЯЖЕЛОГО ШАРИКА
- метод сопряженных градиентов
- МЕТОД НЕСТЕРОВА
- стохастический градиентный спуск
Список методов второго порядка (выбрать один):
- МЕТОД НЬЮТОНА
- демпфированный метод Ньютона
- метод Левенберга–Марквардта
""")

from methods import optimization_loop, gradient_descent, nesterov, heavy_ball, newton
from examples import *

methods = [
    gradient_descent,
    nesterov,
    heavy_ball,
    newton,
]

while True:
    print("Выберите точность (1 - 1e-3, 2 - 1e-6, 3 - 1e-9):")
    try: 
        decision = int(input())
    except:
        print("Введено недопустимое значение, повторите ввод")
        continue
    if decision not in [1, 2, 3]:
        print("Введено недопустимое значение, повторите ввод")
        continue
    epsilon = 1e-3 ** decision
    break

for expr in expressions:
    print()
    print("-" * 96)
    print(expr)
    print("-" * 96)

    for method in methods:
        print()
        print(optimization_loop(method, expr, epsilon))
        print("-" * 96)
    input()
