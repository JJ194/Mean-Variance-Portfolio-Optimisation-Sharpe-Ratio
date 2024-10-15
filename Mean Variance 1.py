import numpy as np
import pandas as pd
import yfinance as yf 
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def download_price_data(ticker, retries=5, delay=7):
    for i in range(retries):
        try:
            price_data = yf.download(ticker, start="2020-01-01", end="2023-01-01")
            return price_data
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")
            time.sleep(delay)
    return None

tickers = input("Enter stock tickers in capital letters and separated by commas(NO SPACES): ").split(",")
tickers = [ticker.strip() for ticker in tickers]  
price_data = yf.download(tickers, start='2018-01-01', end='2023-01-01')['Adj Close']

returns = price_data.pct_change().dropna()
mean_returns = returns.mean() * 252  
cov_matrix = returns.cov() * 252 


num_portfolios = 5000
results = np.zeros((3, num_portfolios))

for i in range(num_portfolios):
    weights = np.random.random(len(tickers))
    weights /= np.sum(weights) 

    portfolio_return = np.sum(weights * mean_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility

    results[0,i] = portfolio_return
    results[1,i] = portfolio_volatility
    results[2,i] = sharpe_ratio

max_sharpe_idx = np.argmax(results[2])
max_sharpe_return = results[0,max_sharpe_idx]
max_sharpe_volatility = results[1,max_sharpe_idx]

min_vol_idx = np.argmin(results[1])
min_vol_return = results[0,min_vol_idx]
min_vol_volatility = results[1,min_vol_idx]


def portfolio_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(weights * mean_returns)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return returns, volatility

def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0):
    p_return, p_volatility = portfolio_performance(weights, mean_returns, cov_matrix)
    return -(p_return - risk_free_rate) / p_volatility

def minimize_volatility(weights, mean_returns, cov_matrix):
    return portfolio_performance(weights, mean_returns, cov_matrix)[1]


constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
bounds = tuple((0, 1) for _ in range(len(tickers)))

initial_guess = len(tickers) * [1./len(tickers)]
optimal_sharpe = minimize(negative_sharpe_ratio, initial_guess,
                          args=(mean_returns, cov_matrix),
                          method='SLSQP', bounds=bounds, constraints=constraints)


optimal_volatility = minimize(minimize_volatility, initial_guess,
                                args=(mean_returns, cov_matrix),
                              method='SLSQP', bounds=bounds, constraints=constraints)


plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='YlGnBu', marker='o')
plt.title('Mean Variance')
plt.xlabel('Volatility (Risk)')
plt.ylabel('Return')
plt.colorbar(label='Sharpe Ratio')

plt.scatter(max_sharpe_volatility, max_sharpe_return, marker='*', color='r', s=200, label='Max Sharpe Ratio')
plt.scatter(min_vol_volatility, min_vol_return, marker='*', color='b', s=200, label='Min Volatility')
plt.legend(labelspacing=0.8)

plt.show()


print("Optimal weights for Max Sharpe Ratio Portfolio:", optimal_sharpe['x'])
print("Expected return, volatility, and Sharpe Ratio for Max Sharpe:", portfolio_performance(optimal_sharpe['x'], mean_returns, cov_matrix))

print("Optimal weights for Min Volatility Portfolio:", optimal_volatility['x'])
print("Expected return and volatility for Min Vol:", portfolio_performance(optimal_volatility['x'], mean_returns, cov_matrix))