import yfinance as yf

def get_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.info['currentPrice']

print(get_price('AAPL'))