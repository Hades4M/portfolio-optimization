import pytest
import numpy as np
import pandas as pd

from src.optimizer import (
    _portfolio_return,
    _portfolio_volatility,
    _negative_sharpe_ratio,
    _weights_constraint,
    optimize_portfolio,
)


def test_portfolio_return():

    weights = np.array([0.5, 0.5])

    expected_returns = pd.Series(
        {
            "A": 0.10,
            "B": 0.20,
        }
    )

    portfolio_return = _portfolio_return(
        weights,
        expected_returns,
    )

    assert np.isclose(
    portfolio_return,
    0.15,
    )

def test_portfolio_volatility():

    weights = np.array([0.5, 0.5])

    covariance_matrix = pd.DataFrame(
        [
            [0.04, 0.00],
            [0.00, 0.09],
        ],
        index=["A", "B"],
        columns=["A", "B"],
    )

    portfolio_volatility = _portfolio_volatility(
        weights,
        covariance_matrix,
    )

    expected = np.sqrt(0.0325)

    assert np.isclose(
        portfolio_volatility,
        expected,
    )


def test_negative_sharpe_ratio():

    weights = np.array([0.5, 0.5])

    expected_returns = pd.Series(
        {
            "A": 0.10,
            "B": 0.20,
        }
    )

    covariance_matrix = pd.DataFrame(
        [
            [0.04, 0.00],
            [0.00, 0.09],
        ],
        index=["A", "B"],
        columns=["A", "B"],
    )

    sharpe = _negative_sharpe_ratio(
        weights,
        expected_returns,
        covariance_matrix,
        risk_free_rate=0.0,
    )

    expected = -(0.15 / np.sqrt(0.0325))

    assert np.isclose(
        sharpe,
        expected,
    )


def test_weights_constraint():

    weights = np.array(
        [0.2, 0.3, 0.5]
    )

    assert _weights_constraint(
        weights
    ) == 0.0


def test_optimize_portfolio():

    expected_returns = pd.Series(
        {
            "A": 0.12,
            "B": 0.18,
            "C": 0.10,
        }
    )

    covariance_matrix = pd.DataFrame(
        [
            [0.04, 0.01, 0.00],
            [0.01, 0.09, 0.01],
            [0.00, 0.01, 0.02],
        ],
        index=["A", "B", "C"],
        columns=["A", "B", "C"],
    )

    weights = optimize_portfolio(
        expected_returns,
        covariance_matrix,
    )

    assert isinstance(
        weights,
        pd.Series,
    )

    assert np.isclose(
        weights.sum(),
        1.0,
    )

    assert np.all(
        weights >= 0.0
    )

    assert np.all(
        weights <= 1.0
    )

    assert len(weights) == 3