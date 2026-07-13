import pandas as pd


def calculate_returns(
    prices: pd.DataFrame,
) -> pd.DataFrame:
    """
    Calculate daily percentage returns.

    Parameters
    ----------
    prices : pd.DataFrame
        Daily closing prices.

    Returns
    -------
    pd.DataFrame
        Daily percentage returns.
    """

    if not isinstance(prices, pd.DataFrame):
        raise TypeError(
            "Prices must be a pandas DataFrame."
        )

    if prices.empty:
        raise ValueError(
            "Prices DataFrame cannot be empty."
        )

    returns = prices.pct_change()

    returns = returns.iloc[1:]

    return returns