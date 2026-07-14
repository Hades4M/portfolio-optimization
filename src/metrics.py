import numpy as np
import pandas as pd


TRADING_DAYS_PER_YEAR = 252


def calculate_annual_return(
    returns: pd.DataFrame,
) -> pd.Series:

    if not isinstance(returns, pd.DataFrame):
        raise TypeError(
            "Returns must be a pandas DataFrame."
        )

    if returns.empty:
        raise ValueError(
            "Returns DataFrame cannot be empty."
        )

    annual_return = (
        returns.mean() * TRADING_DAYS_PER_YEAR
    )

    return annual_return


def calculate_annual_volatility(
    returns: pd.DataFrame,
) -> pd.Series:

    if not isinstance(returns, pd.DataFrame):
        raise TypeError(
            "Returns must be a pandas DataFrame."
        )

    if returns.empty:
        raise ValueError(
            "Returns DataFrame cannot be empty."
        )

    annual_volatility = (
        returns.std() * np.sqrt(TRADING_DAYS_PER_YEAR)
    )

    return annual_volatility


def calculate_annual_covariance_matrix(
    returns: pd.DataFrame,
) -> pd.DataFrame:

    if not isinstance(returns, pd.DataFrame):
        raise TypeError(
            "Returns must be a pandas DataFrame."
        )

    if returns.empty:
        raise ValueError(
            "Returns DataFrame cannot be empty."
        )

    annual_covariance_matrix = (
        returns.cov() * TRADING_DAYS_PER_YEAR
    )

    return annual_covariance_matrix


__all__ = [
    "calculate_annual_return",
    "calculate_annual_volatility",
    "calculate_covariance_matrix",
]