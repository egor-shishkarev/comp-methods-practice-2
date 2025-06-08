class ConsoleHelper:
    def __init__(self, coords, grad_norm, iterations, elapsed_time, method):
        self.coords = coords
        self.grad_norm = grad_norm
        self.iterations = iterations
        self.elapsed_time = elapsed_time
        self.method = method

    def __str__(self):
        s = (f"Результаты метода {self.method}: "
             f"Вычисленное значение минимума = {[round(float(coord), 6) for coord in self.coords]}\n"
             f"Норма градиента = {self.grad_norm:.6f}\n"
             f"Всего итераций = {self.iterations}\n"
             f"Время выполнения = {self.elapsed_time:.3f} секунд\n")
        return s