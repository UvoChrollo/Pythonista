import numpy as np


def list_to_matrices(list_of_value: list, shaping: tuple) -> np.ndarray:
    """merubah list menjadi matriks

    Args:
        list_of_value (list): list nilai-nilai yang ingin dijadikan matriks
        shaping (tuple): ukuran matriks yang diinginkan

    Returns:
        np.ndarray: matriks

    >>> print(list_to_matrices([1,2,3,4],(2,2)))
    [[1 2]
     [3 4]]
    """
    result = np.array(list_of_value).reshape(shaping)
    return result


def desc_stat_matr(matrix: np.ndarray) -> dict:
    """mendapatkan statistika deskriptif dari masing-masing baris dan kolom matriks

    Args:
        matrix (np.ndarray): matrix yang ingin dihitung, anda bisa memakai fungsi list_to_matrices()

    Returns:
        dict : dictionary keterangan statistika deskriptif

    >>> print(desc_stat_matr((list_to_matrices([1,2,3,4],(2,2)))))
    {'row_mean': [1.5, 3.5], 'col_mean': [2.0, 3.0], 'row_median': [1.5, 3.5], 'col_median': [2.0, 3.0], 'row_std': [0.5, 0.5], 'col_std': [1.0, 1.0]}
    """
    shape = matrix.shape
    desc_stat = {
        "row_mean": [np.mean(matrix[row].tolist()) for row in range(0, shape[0])],
        "col_mean": [np.mean(matrix[:, col].tolist()) for col in range(0, shape[1])],
        "row_median": [np.median(matrix[row].tolist()) for row in range(0, shape[0])],
        "col_median": [
            np.median(matrix[:, col].tolist()) for col in range(0, shape[1])
        ],
        "row_std": [np.std(matrix[row].tolist()) for row in range(0, shape[0])],
        "col_std": [np.std(matrix[:, col].tolist()) for col in range(0, shape[1])],
    }
    return desc_stat
