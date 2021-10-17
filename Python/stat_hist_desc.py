import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from typing import Optional


def stat_hist_desc(
    column: pd.Series, data: pd.DataFrame, hue: Optional[pd.Series] = None
):

    """Fungsi untuk menampilkan Histogram beserta informasi tentang Mean, Median, Standard Deviasi

    >>> stat_hist_desc(x=df_mpg['acceleration'],data=df_mpg) # doctest: +SKIP
    """
    if column.isnull().sum() > 0:
        raise ValueError("Maaf, Masih terdapat data yang kosong")

    ax = sns.histplot(x=column, data=data, hue=hue)

    plt.axvline(
        np.mean(column),
        color="r",
        linestyle="--",
        linewidth=1.5,
        label="Mean = {:.2f}".format(np.mean(column)),
    )
    plt.axvline(
        np.median(column),
        color="b",
        linestyle="--",
        linewidth=1.5,
        label="Median = {:.2f}".format(np.median(column)),
    )
    plt.axvline(
        np.std(column),
        color="y",
        linestyle="--",
        linewidth=1.5,
        label="Std.Dev ={:.2f}".format(np.std(column)),
    )

    plt.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.15),
        ncol=3,
        fancybox=True,
        shadow=True,
    )
    plt.show()
