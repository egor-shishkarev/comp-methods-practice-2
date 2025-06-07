from prettytable import PrettyTable
import matplotlib.pyplot as plt

class ConsoleHelper:
    def __init__(self, x_values, u_values, errors, n):
        self.x_values = x_values
        self.u_values = u_values
        self.errors = errors
        self.n = n

    def __str__(self):
        table = PrettyTable(['Кол-во делений отрезка', 'Максимальная погрешность'])
        for n, error in self.errors.items():
            table.add_row([n, error])
        
        s = f"Результаты решения краевой задачи:\n"
        s += f"Количество делений отрезка: {self.n}\n"
        s += f"Таблица погрешностей:\n{table}\n"
        return s 
    
def plot_error(errors, title_add):
    """Построение графика зависимости погрешности от размера сетки"""
    plt.figure(figsize=(10, 6))
    plt.title('Зависимость погрешности от кол-ва делений' + title_add)
    plt.xlabel('Количество делений отрезка')
    plt.ylabel('Погрешность')
    plt.xscale('log', base=10)
    plt.yscale('log', base=10)
    plt.grid(True)
    plt.plot(sorted(errors.keys()), [errors[i] for i in sorted(errors.keys())], 'o-')
    plt.show()

def plot_solution(x_values, u_values, title_add):
    """Построение графика численного решения"""
    plt.figure(figsize=(10, 6))
    plt.title(f'Приближение функции u(x)' + title_add)
    plt.xlabel('x')
    plt.ylabel('u')
    plt.grid(True)

    x = [x_values[i] for i in range(len(x_values))]
    u = [u_values[i] for i in range(len(x_values))]

    plt.plot(x, u)
    plt.show() 