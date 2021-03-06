from datetime import datetime


def str_to_date(masukkan: str, format: str) -> datetime:
    """fungsi untuk merubah string menjadi fungsi

    Args:
        masukkan (str): masukkan input
        format (str): format datetime

    Returns:
        datetime: output berupa tanggal

    >>> print(str_to_date('03/10/2021','%d/%m/%Y'))
    2021-10-03 00:00:00
    """
    hasil = datetime.strptime(masukkan, format)
    return hasil


print(str_to_date("03/10/2021", "%d/%m/%Y"))
