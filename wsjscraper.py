import requests
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen
import re
#https://investoracademy.org/top-10-fundamental-analysis-indicators-for-all-investors/ -> good fundamental analysis indicators
#https://www.getsmarteraboutmoney.ca/invest/investment-products/stocks/6-indicators-used-to-assess-stocks/ -> same thing but with formulas

ticker = 'ORCL'
url = f"https://www.wsj.com/market-tds/quotes/{ticker}/financials/annual/income-statement"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')
tds = soup.find_all('td')
trs = soup.find_all('tr')

def get_EPS(ticker):
    url = f"https://www.wsj.com/market-tds/quotes/{ticker}/financials/annual/income-statement"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage,'html.parser')
    tds = soup.find_all('td', class_='')

    for ttds in tds:
        if ttds.find(text=re.compile("EPS (Basic)")):
                title = ttds.text
                ratio = ttds.parent.find_all('td')[1].text
    print(title)
    print(ratio)

#get_EPS(ticker)

for td in tds:
    for tr in td:
        if tr.text == "EPS (Basic)":
            print(tr)

for td in trs:
    if td.text == "EPS (Basic)":
        print(td.parent.find_all('td')[1].text) #prints EPS ratio
#for ttds in tds:
#    if ttds.find(text=re.compile("Net Income")): #find net income element
#        if (ttds.text == "Consolidated Net Income"):
#            continue
#        elif (ttds.text == "Net Income"):
#            title = ttds.text # str is net income text 
#            continue
#        else:
#            incomeNum = ttds.parent.find_all('td')[1].text #returns net income number
#print(title)
#print(incomeNum)

##def get_net_income(ticker):
#    url = f"https://www.wsj.com/market-tds/quotes/{ticker}/financials/annual/income-statement"
#    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#    webpage = urlopen(req).read()
#    soup = BeautifulSoup(webpage,'html.parser')
#    tds = soup.find_all('td')
#
#    for ttds in tds:
#        if ttds.find(text=re.compile("Net Income")): #find net income element
#             if (ttds.text == "Consolidated Net Income"):
#                continue
#            elif (ttds.text == "Net Income"):
#                title = ttds.text # str is net income text 
#                continue
#            else:
#                incomeNum = ttds.parent.find_all('td')[1].text #returns net income number
#    print(title)
#    print(incomeNum)
#
#get_net_income(ticker)

#Liabilities = table[1] #first instance of <table> this will be the LIABILITIES dropdown
#be sure to add exception catching if table = [] from denied request to WSJ (list index out of range)
#wait maybe 10 seconds between in each call?


#-> Stuff for ASSETS in BALANCE SHEET
#for row in table
#    table[1].find('td').text
#Assets = table[0] #first instance of <table> this will be the ASSETS dropdown
#tableBody = Assets.find('tbody')
#tableRows = tableBody.find_all('tr')
