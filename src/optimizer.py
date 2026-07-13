import numpy as np
import pandas as pd

from scipy.optimize import minimize


def _portfolio_return(
    weights: np.ndarray,
    expected_returns: pd.Series,
) -> float:
    """
    Calculate expected annual portfolio return.

    Parameters
    ----------
    weights : np.ndarray
        Portfolio weights.
    expected_returns : pd.Series
        Annual expected returns.

    Returns
    -------
    float
        Expected portfolio return.
    """

    return float(np.dot(weights, expected_returns))


def _portfolio_volatility(
    weights: np.ndarray,
    covariance_matrix: pd.DataFrame,
) -> float:
    """
    Calculate annual portfolio volatility.

    Parameters
    ----------
    weights : np.ndarray
        Portfolio weights.
    covariance_matrix : pd.DataFrame
        Annual covariance matrix.

    Returns
    -------
    float
        Portfolio volatility.
    """

    return float(
        np.sqrt(
            weights.T @ covariance_matrix @ weights
        )
    )


def _negative_sharpe_ratio(
    weights: np.ndarray,
    expected_returns: pd.Series,
    covariance_matrix: pd.DataFrame,
    risk_free_rate: float,
) -> float:
    """
    Calculate the negative Sharpe ratio.
    """

    portfolio_return = _portfolio_return(
        weights,
        expected_returns,
    )

    portfolio_volatility = _portfolio_volatility(
        weights,
        covariance_matrix,
    )

    if portfolio_volatility <= 0:
        return np.inf

    sharpe_ratio = (
        portfolio_return - risk_free_rate
    ) / portfolio_volatility

    return -sharpe_ratio


def _weights_constraint(
    weights: np.ndarray,
) -> float:
    """
    Ensure that portfolio weights sum to one.
    """

    return np.sum(weights) - 1.0


def optimize_portfolio(
    expected_returns: pd.Series,
    covariance_matrix: pd.DataFrame,
    risk_free_rate: float = 0.0,
) -> pd.Series:
    """
    Optimize portfolio weights by maximizing the Sharpe ratio.

    Parameters
    ----------
    expected_returns : pd.Series
        Annual expected returns.
    covariance_matrix : pd.DataFrame
        Annual covariance matrix.
    risk_free_rate : float, optional
        Annual risk-free rate.

    Returns
    -------
    pd.Series
        Optimal portfolio weights.
    """

    if not isinstance(expected_returns, pd.Series):
        raise TypeError(
            "Expected returns must be a pandas Series."
        )

    if not isinstance(covariance_matrix, pd.DataFrame):
        raise TypeError(
            "Covariance matrix must be a pandas DataFrame."
        )

    if expected_returns.empty:
        raise ValueError(
            "Expected returns cannot be empty."
        )

    if covariance_matrix.empty:
        raise ValueError(
            "Covariance matrix cannot be empty."
        )

    if covariance_matrix.shape[0] != covariance_matrix.shape[1]:
        raise ValueError(
            "Covariance matrix must be square."
        )

    if not expected_returns.index.equals(
        covariance_matrix.index
    ):
        raise ValueError(
            "Expected returns and covariance matrix must contain the same assets."
        )

    if not covariance_matrix.index.equals(
        covariance_matrix.columns
    ):
        raise ValueError(
            "Covariance matrix rows and columns must match."
        )

    n_assets = len(expected_returns)

    initial_weights = np.ones(n_assets) / n_assets

    bounds = [(0.0, 1.0)] * n_assets

    constraints = (
        {
            "type": "eq",
            "fun": _weights_constraint,
        },
    )

    result = minimize(
        fun=_negative_sharpe_ratio,
        x0=initial_weights,
        args=(
            expected_returns,
            covariance_matrix,
            risk_free_rate,
        ),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    if not result.success:
        raise RuntimeError(result.message)

    return pd.Series(
        result.x,
        index=expected_returns.index,
        name="Weight",
    )


__all__ = [
    "optimize_portfolio",
]