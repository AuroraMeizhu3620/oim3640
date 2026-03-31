# #typing: removing ambiguity
# ##(s:str)
# import yfinance as yf
# from pprint import pprint
# tickers = {'AAPL', 'NVDA', 'MSFT', 'META', 'GOOG'}
# stocks = {}

# for t in tickers:
#     stocks[t] = yf.Ticker(t).info['currentPrice']

# print(stocks)

# print('After sorting...')

#def sort_by_price(t):
    #return t[1] # sort by the second item in the tuple
#print(sorted(stocks.items(), key = sort_by_price))
# print(sorted(stocks.items(), key = lambda t: t[1])) # anonymous to function above

# #Error Handling
# num = 100
# #except = robtic filtering of mistakes
# try:
#     a = float(input('Enter a number to divide by:'))
#     print(num/a)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.") #filtering errors
# except ValueError:
#     print("Error: Please enter a valid number.") #filtering errors
# finally: #does not matter, always gets here
#     print('We still want to print this!')

# names = ['Alice', 'Bob', 123, 'Charlie'] #does not realize 123
# uppercase_names = []

# for name in names:
#     try:
#         print(name.upper())
#         uppercase_names.append(name.upper())
#     except AttributeError:
#         print(f"Error: '{name}' is not a string and cannot be converted to uppercase.")

# print("Uppercase names:", uppercase_names)

###use cases: 
# When something is out of your control
# 1) when user is inputting something and you do not want program to stop
# 2) when you are reading file and getting errors
# 3) io, input output
# 4) connecting to APIs
###

#What is API and how to connect to API
## user send HTTP request to API, API responds JSON
## https entered as URL, https 'get' request sent to server, response from the server
# import requests
# response = requests.get('https://oim.108122.xyz/words/random')
# print(response.json())

import requests
response = requests.get(
    'https://oim.108122.xyz/echo',
    headers={'X-Token':'meizhumeizhu'},
)
print(response.json())
data = response.json() #usually a long response, .json convert big stream to well-structured data type

# print(data['name'])
# print(data['governor'])

#data structure exploration
print(len(data))
print(data.keys())
# print(type(data['data']))

# towns = data['data']
# print(type(towns))
# print(len(towns))

# for town in data['data'][:5]:
#     print(f"{town['name']}: pop {town['population']:,}")

# #find town with smallest population
# smallest = min(towns, key=lambda t: t['population'])
# print(f"Smallest town: {smallest['name']} with population {smallest['population']:,}")
