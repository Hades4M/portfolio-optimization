import aiohttp
import aiomoex
import pandas as pd

REQUIRED_COLUMNS = ("TRADEDATE","CLOSE")
    
DEFAULT_START_DATE = "2010-01-01"

async def load_history(
    ticker: str,
    start_date: str = DEFAULT_START_DATE,
) -> pd.DataFrame:
    """
    Download historical prices from MOEX.

    Parameters
    ----------
    ticker : str
        MOEX ticker.
    start_date : str, optional
        First date to keep (YYYY-MM-DD).

    Returns
    -------
    pd.DataFrame
        Historical prices indexed by TRADEDATE.
    """

    ticker = ticker.strip().upper() #адекватная проверка тикера
    if not ticker:
        raise ValueError("Ticker cannot be empty.")

    async with aiohttp.ClientSession() as session:
        data = await aiomoex.get_board_history(session, ticker)
        df = pd.DataFrame(data)

    if df.empty:
        raise ValueError(f"MOEX returned no historical data for ticker '{ticker}'.")

    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            raise ValueError(f"MOEX response does not contain required column '{column}'.")

    df["TRADEDATE"] = pd.to_datetime(df["TRADEDATE"])
    df = df.set_index("TRADEDATE")

    df = df[df.index >= start_date]

    return df


async def load_close_prices(tickers: list[str],) -> pd.DataFrame:
    
    if not tickers:
        raise ValueError("Ticker list cannot be empty")
    
    price_series = []

    for ticker in tickers:
        history = await load_history(ticker)

        close_prices = history["CLOSE"]
        close_prices = close_prices.rename(ticker)

        price_series.append(close_prices)

    prices = pd.concat(price_series, axis=1)

    return prices

__all__ = [
    "load_history",
    "load_close_prices",
]