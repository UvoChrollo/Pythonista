from datetime import datetime


def string_to_datetime(masukkan: str, format: str) -> datetime:
    """merubah string jadi datetime

    Args:
        masukkan (str): tanggal yang akan diubah
        format (str): format yang di-inginkan

    Returns:
        datetime: hasil akhir tanggal

    >>> string_to_datetime('18/09/19','%d/%m%y')
    18/09/19
    """
    date_obj = datetime.strptime(masukkan, format)
    return date_obj
