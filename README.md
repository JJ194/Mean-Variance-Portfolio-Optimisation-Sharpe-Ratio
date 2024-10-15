# Mean-Variance-Portfolio-Optimisation-Sharpe-Ratio
I began by importing the relevant libraries. I determined I would need to use numpy, pandas, yfinance, matplotlib, and scipy.

![image](https://github.com/user-attachments/assets/587efc50-afa3-493d-9dce-f60876a7f456)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I then defined a function to download historical price data with error handling to combat an error I had encountered when trying to run the program earlier.

![image](https://github.com/user-attachments/assets/a024c927-2f90-4c58-8d33-1b3d082f03ec)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I then prompt the user for tickers and downloaded the adjusted close prices.

![image](https://github.com/user-attachments/assets/d84e2cab-893c-442c-a192-433172ea487e)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I then programmed a function to calculate daily percentage changes and then calculate the annualized mean returns and the covariance matrix of returns, which are essential inputs for portfolio optimization.

![image](https://github.com/user-attachments/assets/64ee639b-ae0c-4eb9-b8ec-5fb7230cd56c)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I then generated random portfolios and stored their returns, volatility, and Sharpe ratios.

![image](https://github.com/user-attachments/assets/79aba1dc-1b42-4176-b3d2-4187c603f15a)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I then found the portfolios with the maximum Sharpe ratio and minimum volatility.

![image](https://github.com/user-attachments/assets/068204c1-4363-4656-b8bb-5e9086790b75)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I then defined the functions used to calculate the portfolio performance, negative Sharpe ratio and minimising volatility.

![image](https://github.com/user-attachments/assets/d25a18ac-996a-4dd3-ae98-6f623b3088df)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I then programmed constraints for the project to ensure that the weights sum to 1.

![image](https://github.com/user-attachments/assets/3a6b9216-006c-4aa9-bb98-eab3a848509e)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I then programmed a function to plot the data that shows the trade off between risk and return for the various portfolios. The optimal portfolios are highlighted when you run the code.

![image](https://github.com/user-attachments/assets/498f5a14-4f4a-48e8-b8ba-aca7af6942a1)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Finally, the data for the optimal weights for the max Sharpe ratio, minimum volatility and expected returns with their volatility are outputted into the console.

![image](https://github.com/user-attachments/assets/fafac3f6-d0c4-49c7-9dca-b11c9d5c34a9)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<b>I plan in future to add an interactive GUI for the user and display updated price data on the tickers the user inputs<b>
