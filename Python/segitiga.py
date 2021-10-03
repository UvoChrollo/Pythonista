def segitiga(a: int, t: int) -> int:
    """fungsi untuk menghitung luas segitiga

    Args:
        a (int): alas segitiga yang diketahui
        t (int): tinggi segitiga yang diketahui

    Returns:
        int: luas segitiga

    >>> segitiga(2,3)
    3
    """
    return (a * t) // 2
