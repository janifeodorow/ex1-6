#exercise 6
import yfinance as yf
import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt

gme_ticker = yf.Ticker("GME")
gme_data = gme_ticker.history(period="max")
gme_data.reset_index(inplace=True)
gme_data['Date'] = pd.to_datetime(gme_data['Date'])

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.text


tables = pd.read_html(StringIO(html_data))

gme_revenue = tables[1]
gme_revenue.columns = ["Date", "Revenue"]
gme_revenue["Revenue"] = gme_revenue["Revenue"].astype(str).str.replace(r',|\$', "", regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]

gme_revenue['Date'] = pd.to_datetime(gme_revenue['Date'])
gme_revenue['Revenue'] = gme_revenue['Revenue'].astype(float)

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

make_graph(gme_data, gme_revenue, 'GameStop')