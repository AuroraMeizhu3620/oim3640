import timeit
words = open('data/words.txt').read().split()
word_set = set(words)

def search_list():
    return 'python' in words
def search_set():
    return 'python' in word_set

print('List:', timeit.timeit(search_list, number = 1000))
print('Set', timeit.timeit(search_set, number = 1000))


# import yfinance as yf
# # stock = yf.Ticker('AAPL')


# # for k, v in info.items():
# #     print(k,v)

# tickers = ['AAPL', 'NVDA', 'MSFT', 'META', 'GOOG']
# stocks = {}
# info = stocks.info

# for t in tickers:
#     stocks[t] = yf.Ticker(t).info['open'], stocks[t] = yf.Ticker(t).info['currentPrice'],stocks[t] = yf.Ticker(t).info['volume']
# print(stocks)


# tickers = ['APPL', 'NVDA', 'MSFT']
# prices = {}
# for t in tickers:
#     prices[t] = yf.Ticker(t).info['currentPrice']
    

# print(prices)

# print(sorted(prices.values(), reverse = True))# create a new list of the keys in prices

# company = input('What company do you wish to learn about:')
# ask = input('What about the company o you wish to learn about:')

# stock = yf.Ticker("AAPL")
# info = stock.info
# print(type(info))

# print(info.keys())
# print(len(info))


# print(info['shortName'])
# print(info['longName'])
# print(info['currentPrice'])

# #print(info['longBusinessSummary'])

# #print((info['longBusinessSummary']).split())

# print('iPhone' in info['longBusinessSummary'])

# info['city']='Wellesley'
# print(info['city'])

# info['founder'] = 'Robert'
# print(info['founder'])
