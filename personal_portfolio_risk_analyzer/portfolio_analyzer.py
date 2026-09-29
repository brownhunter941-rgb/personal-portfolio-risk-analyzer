import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample portfolio weights
WEIGHTS = {
    "SPY": 0.50,
    "QQQ": 0.30,
    "BND": 0.20,
}

prices = pd.read_csv("portfolio_prices.csv", parse_dates=["Date"])
prices = prices.set_index("Date")

# Daily percentage returns
returns = prices.pct_change().dropna()

# Portfolio daily returns
weights = pd.Series(WEIGHTS)
portfolio_returns = returns[list(WEIGHTS)].dot(weights)

# Annualized metrics
trading_days = 252
asset_annual_return = returns.mean() * trading_days
asset_annual_volatility = returns.std() * np.sqrt(trading_days)

portfolio_annual_return = portfolio_returns.mean() * trading_days
portfolio_annual_volatility = portfolio_returns.std() * np.sqrt(trading_days)

print("\nINDIVIDUAL ASSETS")
print("-" * 50)
for asset in WEIGHTS:
    print(
        f"{asset}: return={asset_annual_return[asset]:.2%}, "
        f"volatility={asset_annual_volatility[asset]:.2%}"
    )

print("\nPORTFOLIO")
print("-" * 50)
print(f"Expected annualized return: {portfolio_annual_return:.2%}")
print(f"Annualized volatility:      {portfolio_annual_volatility:.2%}")

# Growth of $10,000
growth = (1 + portfolio_returns).cumprod() * 10000

plt.figure(figsize=(9, 5))
plt.plot(growth.index, growth.values)
plt.title("Growth of a $10,000 Sample Portfolio")
plt.xlabel("Date")
plt.ylabel("Portfolio Value ($)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("portfolio_growth.png", dpi=160)
plt.show()
