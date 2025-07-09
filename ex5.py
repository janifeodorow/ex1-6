#exercise 5
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO
import matplotlib.pyplot as plt

tesla_ticker = yf.Ticker("TSLA")
tesla_data = tesla_ticker.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data['Date'] = pd.to_datetime(tesla_data['Date'])

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.text

tables = pd.read_html(StringIO(html_data))

tesla_revenue = tables[1]
tesla_revenue.columns = ["Date", "Revenue"]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].astype(str).str.replace(r',|\$', "", regex=True)

tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]

tesla_revenue['Date'] = pd.to_datetime(tesla_revenue['Date'])
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].astype(float)

def make_graph(stock_data, revenue_data, stock_name):
    fig, ax1 = plt.subplots(figsize=(14,7))

    ax1.plot(stock_data['Date'], stock_data['Close'], color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Stock Price ($)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(revenue_data['Date'], revenue_data['Revenue'], color='green')
    ax2.set_ylabel('Revenue (Millions)', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    plt.xlim(left=stock_data['Date'].min(), right=pd.to_datetime('2021-06-30'))
    plt.title(f"{stock_name} Stock Price and Revenue Over Time")
    plt.show()

make_graph(tesla_data, tesla_revenue, 'Tesla')