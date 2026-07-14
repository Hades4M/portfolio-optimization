import pytest
import pandas as pd
from src.returns import calculate_returns


def test_calculate_returns():
    prices = pd.DataFrame(
        {
            "A": [100, 110, 121],
        }
    )

    returns = calculate_returns(prices)

    expected = pd.DataFrame(
        {
            "A": [0.10, 0.10],
        },
        index=[1, 2],
    )

    pd.testing.assert_frame_equal(
        returns,
        expected,
    )
