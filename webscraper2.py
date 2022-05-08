from bs4 import BeautifulSoup 
import requests
##Stocks
url_financials = "https://finance.yahoo.com/quote/{}/financials?p={}"
url_stats = "https://finance.yahoo.com/quote/{}/key-statistics?p={}"

stock = 'TSLA'

response = requests.get(url_financials.format(stock, stock))

soup = BeautifulSoup(response.text, 'html.parser')



##CryptoCurrency
url_summary = "https://finance.yahoo.com/quote/ETH-USD?p=ETH-USD"
url_historicalData = "https://finance.yahoo.com/quote/ETH-USD/history?p=ETH-USD"

