import time
from scipy import sparse
from functools import wraps
import numpy as np


def to_sparse(array, dtype=None) -> sparse:
    """Converts a given array to a sparse matrix.

    :param array: The array to convert.
    :type array: np.ndarray
    :param dtype: The data type of the sparse matrix. If None, the data type of the array is used.
    :type dtype: type
    :return: The sparse matrix.
    :rtype: sparse
    """
    if dtype is None:
        return sparse.csr_array(array)
    else:
        return sparse.csr_array(array, dtype=dtype)


Sx = to_sparse(np.array([[0, 1], [1, 0]])/2)
Sy = to_sparse(np.array([[0, -1], [1, 0]])/2)
Sz = to_sparse(np.array([[1, 0], [0, -1]])/2)
