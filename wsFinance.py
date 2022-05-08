import requests
from bs4 import BeautifulSoup 

#ticker = input("Enter ticker value:")
#url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"

#def get_price(ticker):
#    url = f"https://finance.yahoo.com/quote/{ticker}/"
#    result = requests.get(url)
#    soup = BeautifulSoup(result.text,'html.parser')
#    price = soup.find("fin-streamer", {"data-symbol": f"{ticker}"})
#    print(float(price.contents[0].replace(',', '')))
#
#tickers = ["ORCL", "GME", "TSLA", "GOOG"]

#for ticker in tickers:
#    get_price(ticker)

#scrape and store into a data structure the text 
#write methods to calculate quick, debt to equity, and debt to assets ratios

def get_quick_ratio(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/balance-sheet?p={ticker}"
    result = requests.get(url, headers={'User-Agent': 'Custom'})
    soup = BeautifulSoup(result.text,'html.parser')
    currAssetsRow = soup.findAll('div', {'class':"D(tbr) fi-row Bgc($hoverBgColor):h"})
    print(currAssetsRow)
get_quick_ratio("GME")

#quick ratio = (current assets - inventory) / current liabilities
#

# TotLiabilities = (soup.findAll("div", {'class': 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)'}, {'data-test': 'fin-col'}))[2]
# totAssets = soup.find("div", {'class': 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)'}, {'data-test': 'fin-col'})
#TotAssetsRow = soup.findAll('div', {'class':"D(tbr) fi-row Bgc($hoverBgColor):h"}) #bs4.element.ResultSet