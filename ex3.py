#exercise 3
import yfinance as yf

gme_ticker = yf.Ticker("GME")

gme_data = gme_ticker.history(period="max")
gme_data.reset_index(inplace=True)

print(gme_data.head())
