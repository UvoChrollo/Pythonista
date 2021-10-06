# p.get_height() = mendapatkan tinggi plot
# p.get_x() = mendapatkan koordinat x dari label
# color = warna tulisan
# size = ukuran tulisan
# ha = horizontal alignment, highly recommend : center
# va = vertical alignment, highly recommend : center


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def count_anno_plot(column: pd.Series, data: pd.DataFrame):
    """fungsi untuk menampilkan countplot sekaligus data

    Args:
        column (pd.Series): nama kolom yang akan tampilkan
        data (pd.DataFrame): nama dataframe

    >>> count_anno_plot(column='Kota',data=daerah) # doctest: +SKIP
    """
    ax = sns.countplot(x=column, data=data)
    for p in ax.patches:
        ax.annotate(
            p.get_height(),
            (p.get_x() + 0.4, p.get_height() - 0.1),
            ha="center",
            va="top",
            color="black",
            size=15,
        )
    plt.show()
