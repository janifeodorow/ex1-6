#exercise 1
import yfinance as yf

tesla = yf.Ticker("TSLA")
tesla_stock_data = tesla.history(period="max")
print(tesla_stock_data.head())