import pytest
import pandas as pd
import numpy as np
from src.metrics import calculate_annual_return
from src.metrics import calculate_annual_volatility
from src.metrics import calculate_annual_covariance_matrix


#Тестирование returns
def test_calculate_annual_return():
    returns = pd.DataFrame(
        {
            "A": [0.01,0.01,0.01,0.01,0.01],
        }
    )

    annual_return = calculate_annual_return(returns)

    expected = pd.Series(
        {
            "A": 0.01 * 252,
        }
    )

    pd.testing.assert_series_equal(
        annual_return,
        expected
    )


def test_calculate_annual_return_empty_dataframe():
    returns = pd.DataFrame()

    with pytest.raises(ValueError):
        calculate_annual_return(returns)

def test_calculate_annual_return_invalid_type():
    with pytest.raises(TypeError):
        calculate_annual_return([1, 2, 3])

#Тестирование volatility
def test_calculate_annual_volatility():
    returns = pd.DataFrame(
        {
            "A": [0.01,0.03,0.02,0.07,0.02],
        }
    )

    annual_volatility = calculate_annual_volatility(returns)

    expected = returns.std()*np.sqrt(252)

    pd.testing.assert_series_equal(
        annual_volatility,
        expected
    )


def test_calculate_annual_volatility_empty_dataframe():
    returns = pd.DataFrame()

    with pytest.raises(ValueError):
        calculate_annual_volatility(returns)

def test_calculate_annual_volatility_invalid_type():
    with pytest.raises(TypeError):
        calculate_annual_volatility([1, 2, 3])

#Тестирование covariance
def test_calculate_annual_covariance_matrix():
    returns = pd.DataFrame(
        {
        "A": [0.01, 0.02, 0.01],
        "B": [0.03, 0.01, 0.02]
        }
    )

    covariance_matrix = calculate_annual_covariance_matrix(returns)

    expected =returns.cov()*252

    pd.testing.assert_frame_equal(
        covariance_matrix,
        expected
    )

def test_calculate_annual_covariance_matrix_empty_dataframe():
    returns = pd.DataFrame()

    with pytest.raises(ValueError):
        calculate_annual_covariance_matrix(returns)

def test_calculate_abbual_covariance_matrix_invalid_type():
    with pytest.raises(TypeError):
        calculate_annual_covariance_matrix([1, 2, 3])
