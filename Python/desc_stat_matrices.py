import numpy as np


def list_to_matrices(list_of_value: list, shaping: tuple) -> np.ndarray:
    """merubah list

    Args:
        list_of_value (list): [description]
        shaping (tuple): [description]

    Returns:
        np.ndarray: [description]

    >>> print(list_to_matrices([1,2,3,4],(2,2)))
    [[1 2]
     [3 4]]
    """
    result = np.array(list_of_value).reshape(shaping)
    return result
