from typing import List
import numpy as np
from numpy.linalg import cond, norm, inv


def get_spectral_condition_number(matrix: List[List[float]]): 
    # тут получается вычисляем обусловленность как произведение нормы матрицы на норму обратной матрицы.
    # если больше 10^4, то все плохо, но есть исключения
    A = np.array(matrix)

    return cond(A)

def get_volume_condition_number(matrix: List[List[float]]):
    # здесь вычисляем как отношение объема параллелепипеда построенного на строках матрицы как на ребрах к объему прямоугольного параллелепипеда с теми же ребрами

    A = np.array(matrix)
    
    determinant = np.abs(np.linalg.det(A))
    if determinant == 0: 
        return np.inf
    
    count_of_rows = A.shape[0]
    row_norms_product = 1

    for i in range(count_of_rows):
        row_norms_product *= np.sqrt(np.sum(A[i] ** 2))

    return row_norms_product / determinant
    

def get_angular_condition_number(matrix: List[List[float]]):
    # величина обратная синусу наименьшего из углов, образованных (N-1)-мерными гранями на ребрах am, и оставшимся ребром an, n != m. 
    # max(|an|, |cn|), опять обратные есть
    A = np.array(matrix)

    A_inv = inv(matrix)
    max_val = 0
    for i in range(A.shape[0]):
        a_n = A[i]
        c_n = A_inv[:, i]
        val = norm(a_n) * norm(c_n)
        max_val = max(max_val, val)

    return max_val

