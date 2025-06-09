import numpy as np
import time

def gradient_descent(func, grad, x0, lr, tol, max_iter):
    """
    Простой (безусловный) градиентный спуск.
    Возвращает (x_min, метрики).
    """
    x = x0.copy()
    metrics = {'iter': 0, 'grad_evals': 0, 'func_evals': 0, 'time': 0.0}
    start = time.time()
    for i in range(max_iter):
        metrics['iter'] += 1
        g = grad(x)
        metrics['grad_evals'] += 1
        if np.linalg.norm(g) < tol:
            break
        x = x - lr * g
        
    metrics['time'] = time.time() - start
    metrics['func_evals'] = metrics['iter'] + 1
    return x, metrics

def gradient_projection(func, grad, x0, eq_cons, ineq_cons=None,
                        lr=0.1, tol=1e-6, max_iter=1000):
    """
    Проекция градиента для линейных равенств psi(x)=0 и (опционально)
    линейных неравенств phi(x)<=0.
    eq_cons = [(psi, grad_psi), ...]
    ineq_cons = [(phi, grad_phi), ...]
    """
    if ineq_cons is None:
        ineq_cons = []

    x = x0.copy()
    # Построим A x = b для равенств psi(x)=0
    if eq_cons:
        A = np.vstack([grad_psi(x0) for _, grad_psi in eq_cons])
        b = np.array([np.dot(grad_psi(x0), x0) - psi(x0)
                      for psi, grad_psi in eq_cons])
        # начальная проекция на равенства
        mu0 = np.linalg.solve(A.dot(A.T), A.dot(x) - b)
        x -= A.T.dot(mu0)
    else:
        A = np.empty((0, x.shape[0]))
        b = np.empty(0)

    metrics = {'iter': 0, 'grad_evals': 0, 'func_evals': 0, 'time': 0.0}
    start = time.time()

    for _ in range(max_iter):
        metrics['iter'] += 1
        g = grad(x)
        metrics['grad_evals'] += 1

        # Проекция градиента на касательное подпространство равенств
        if A.size:
            M = A.dot(A.T)
            lam = np.linalg.solve(M, A.dot(g))
            g_proj = g - A.T.dot(lam)
        else:
            g_proj = g

        # Проверка на сходимость по норме спроецированного градиента
        if np.linalg.norm(g_proj) < tol:
            break

        # Шаг градиентного спуска в касательном подпространстве
        x = x - lr * g_proj

        # Проекция обратно на равенства
        if A.size:
            mu = np.linalg.solve(A.dot(A.T), A.dot(x) - b)
            x = x - A.T.dot(mu)

        # Проекция на полупространство для каждого неравенства
        for phi, dphi in ineq_cons:
            v = phi(x)
            if v > 0:
                grad_phi = dphi(x)
                # ортопроекция на границу phi(x)=0
                x = x - (v / np.dot(grad_phi, grad_phi)) * grad_phi

    metrics['time'] = time.time() - start
    f_val = func(x)
    metrics['func_evals'] = 1
    return x, f_val, metrics

def penalty_method(func, grad, x0, eq_cons, ineq_cons,
                   alpha0=1, alpha_factor=5,
                   lr=0.1, tol=1e-6, max_iter=2000, max_outer=10):
    """
    Штрафной метод: последовательно растим alpha.
    eq_cons = [(psi, grad_psi)], ineq_cons = [(phi, grad_phi)].
    """
    x = x0.copy()
    total = {'iter': 0, 'grad_evals': 0, 'func_evals': 0, 'time': 0.0}
    alpha = alpha0

    for _ in range(max_outer):
        def F(u):
            val = func(u)
            for psi, _ in eq_cons:
                val += alpha * psi(u)**2
            for phi, _ in ineq_cons:
                v = max(0.0, phi(u))
                val += alpha * v*v
            return val

        def dF(u):
            g = grad(u).copy()
            for psi, dpsi in eq_cons:
                g += alpha * 2*psi(u)*dpsi(u)
            for phi, dphi in ineq_cons:
                v = phi(u)
                if v > 0:
                    g += alpha * 2*v*dphi(u)
            return g

        x, m = gradient_descent(F, dF, x, lr, tol, max_iter)

        total['iter']       += m['iter']
        total['grad_evals'] += m['grad_evals']
        total['func_evals'] += m['func_evals']
        total['time']       += m['time']

        # проверка штрафа
        H = sum(psi(x)**2 for psi, _ in eq_cons)
        H += sum(max(0.0, phi(x))**2 for phi, _ in ineq_cons)
        if alpha * H < tol:
            break

        alpha *= alpha_factor

    f_val = func(x)
    total['func_evals'] += 1
    return x, f_val, total

def barrier_method(func, grad, x0, ineq_cons,
                   mu0=1.0, mu_factor=10.0,
                   lr=0.1, tol=1e-6,
                   max_iter=1000, max_outer=10):
    x = x0.copy()
    metrics = {'iter': 0, 'grad_evals': 0, 'func_evals': 0, 'time': 0.0}
    mu = mu0

    # Используем log-барьер: B(x)= -sum(log(-phi_i(x)))
    for outer in range(max_outer):
        def B(u):
            vals = []
            for phi, _ in ineq_cons:
                v = phi(u)
                if v >= 0:
                    return np.inf
                vals.append(-np.log(-v))
            return sum(vals)

        def F(u):
            return func(u) + mu * B(u)

        def dF(u):
            g = grad(u).copy()
            for phi, dphi in ineq_cons:
                v = phi(u)
                g += mu * (dphi(u) / -v)
            return g

        start = time.time()
        for i in range(max_iter):
            gF = dF(x)
            metrics['grad_evals'] += 1
            if np.linalg.norm(gF) < tol:
                break
            t = lr
            # backtracking: сохраняем допустимость
            while True:
                x_new = x - t * gF
                if all(phi(x_new) < 0 for phi, _ in ineq_cons):
                    break
                t *= 0.5
                if t < 1e-12:
                    break
            x = x_new
            metrics['iter'] += 1
        metrics['time'] += time.time() - start
        metrics['func_evals'] += 1

        # внешний критерий: близость к границе phi(x)>=-tol
        if all(phi(x) > -tol for phi, _ in ineq_cons):
            break
        mu /= mu_factor

    f_val = func(x)
    metrics['func_evals'] += 1
    return x, f_val, metrics
