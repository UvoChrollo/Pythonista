from collections import defaultdict


class Makanan:
    """
    >>> m1 = Makanan(2,"Meja 1")
    >>> m1.tambah_menu("Ayam Goreng","Mie Ayam")
    >>> print(m1)
    Menu Ayam Goreng : Harga 20000
    Menu Mie Ayam : Harga 10000
    <BLANKLINE>
    """

    def __init__(self, quantity, nomor_meja):
        self.qty = quantity
        self.meja = nomor_meja
        self.pilihan_menu = []
        self.harga = []

    food_dict = {"Ayam Goreng": 20000, "Nasi Goreng": 12000, "Mie Ayam": 10000}

    food = defaultdict(lambda: "Maaf, Data Tidak Tersedia", food_dict)

    def tambah_menu(self, *makanan):
        if len(makanan) > self.qty:
            keterangan = "Maaf, Data Berlebih"
        elif len(makanan) <= self.qty:
            for x in makanan:
                if x in Makanan.food.keys():
                    self.pilihan_menu.append(x)
                    self.harga.append(Makanan.food[x])
                else:
                    break

    def __str__(self):
        result = ""
        for i in range(self.qty):
            result += "Menu {} : Harga {}\n".format(self.pilihan_menu[i], self.harga[i])
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
