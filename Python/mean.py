def mean(bilangan: list) -> float:
    """fungsi untuk menghitung rata-rata sekumpulan bilangan

    Args:
        bilangan (list): sekumpulan bilangan dalam format list

    Returns:
        float: rata-rata bilangan

    >>> print(mean([1,2,3]))
    2.0
    """
    rata_rata = sum(bilangan) / len(bilangan)
    return rata_rata
