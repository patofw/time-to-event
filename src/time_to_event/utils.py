import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt


def dist_histogram(
        df: pd.DataFrame,
        col: str,
        bins: int = 30,
        hue_: str | None = None,
        **kwargs
):
    """
    Plots a histogram of a specified column from a DataFrame, with optional hue separation.

    This function uses seaborn to create a histogram with an optional kernel density estimate (KDE).
    If a hue column is provided, the data is separated by the hue values.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        col (str): The name of the column to plot.
        bins (int, optional): The number of bins to use in the histogram. Defaults to 30.
        hue_ (str | None, optional): The name of the column to use for hue separation. Defaults to None.
        **kwargs: Additional keyword arguments passed to seaborn's histplot function.

    Returns:
        None
    """
    if not hue_:
        sns.histplot(df[col], bins=bins, kde=True, **kwargs)

    else:
        _df = df[[hue_, col]].melt([hue_], var_name='melt',  value_name='vals')
        sns.histplot(
            data=_df,
            x="vals",
            hue=hue_,
            bins=bins,
            kde=True,
            **kwargs
        )

    plt.title(f'{col} Distribution by {hue_}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()


def countplot(
        df: pd.DataFrame, x: str, stat: str | None = "percent", hue: str | None = None
):
    """
    Plots a count plot of a specified column from a DataFrame, with optional hue separation.

    This function uses seaborn to create a count plot with the option to display counts or percentages.
    If a hue column is provided, the data is separated by the hue values.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        x (str): The name of the column to plot on the x-axis.
        stat (str | None, optional): The statistic to plot, either 'count' or 'percent'. Defaults to 'percent'.
        hue (str | None, optional): The name of the column to use for hue separation. Defaults to None.

    Returns:
        None

    """
    sns.countplot(
        data=df,
        x=x,
        hue=hue,
        stat=stat
    )
    ylabel = str(stat) + " cases"
    plt.title(f'{x} Distribution')
    plt.xlabel(x)
    plt.ylabel(ylabel)
    plt.show()
