![Python](https://img.shields.io/badge/Python-3.11-blue)
![Tests](https://img.shields.io/badge/tests-15%20passed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

# Portfolio Optimization

Portfolio Optimization is a Python project for constructing and optimizing investment 
portfolios using Modern Portfolio Theory (MPT).
The project loads historical market data from the Moscow Exchange (MOEX), calculates portfolio statistics
and finds the optimal portfolio.

## Features

- Load historical prices from MOEX ISS API
- Calculate daily returns
- Calculate annual expected returns
- Calculate annual volatility
- Calculate annual covariance matrix
- Optimize portfolio weights by maximizing the Sharpe ratio (changeable riskless rate)
- Unit tests with pytest

## Project structure

```text
portfolio-optimization/
│
├── notebooks/
│   └── demo.ipynb
│
├── src/
│   ├── loader.py
│   ├── returns.py
│   ├── metrics.py
│   └── optimizer.py
│
├── tests/
│   ├── test_returns.py
│   ├── test_metrics.py
│   └── test_optimizer.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Optimization pipeline and example

Showed in Demo.ipynb

## Tech Stack

- Python
- pandas
- NumPy
- SciPy
- aiohttp
- pytest
- Jupyter Notebook

## Roadmap

Current version:

- Historical data loader
- Portfolio optimization
- Unit tests

Planned:

- Risk-free rate support
- Sharpe ratio metrics
- Efficient Frontier
- Portfolio visualization
- Monte Carlo simulation
- Additional portfolio statistics

## License

MIT License.


