from scipy.optimize import approx_fprime


class Function:
    def __init__(
            self,
            string,
            function,
            dim,
            expected_minimum,
    ):
        self._string = string
        self._function = function
        self._dim = dim
        self._expected_minimum = expected_minimum
        
        self.alpha = 0.01
        self.beta = 0.01
        self.gamma = 0.01

    def __call__(self, *args):
        return self._function(*args)

    def __str__(self):
        return f"Функция: {self._string}, ожидаемый минимум: {self._expected_minimum}"

    def dim(self):
        return self._dim

    def gradient(self, point):
        return approx_fprime(point, self._function)

    def hess(self, point):
        hessian = []
        for i in range(self._dim):
            def grad(point):
                return approx_fprime(point, self._function)[i]

            hessian.append(approx_fprime(point, grad))
        return hessian
