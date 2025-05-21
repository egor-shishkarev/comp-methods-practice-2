from typing import List
import numpy as np
from scipy import sparse

def generate_tridiag_spd(n, a_diag=10.0, a_offdiag=-2.0):
    diags = [
        a_offdiag * np.ones(n-1),
        a_diag     * np.ones(n),
        a_offdiag * np.ones(n-1),
    ]
    offsets = [-1, 0, 1]
    A = sparse.diags(diags, offsets, format='csr')
    return A

def print_matrix(matrix: List[List[float]]):
    print()
    for row in matrix:
        formatted_row = [f"{x:8.3f}" for x in row]
        print("|", " ".join(formatted_row), "|")

