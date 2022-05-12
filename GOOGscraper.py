import requests
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen
import re
#https://investoracademy.org/top-10-fundamental-analysis-indicators-for-all-investors/ -> good fundamental analysis indicators
#https://www.getsmarteraboutmoney.ca/invest/investment-products/stocks/6-indicators-used-to-assess-stocks/ -> same thing but with formulas

ticker = input("Enter the Stock Ticker you'd like financial information on: ")
url = f"https://www.google.com/finance/quote/{ticker}:NYSE?hl=en"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')

pdiv = soup.find_all('div', {'jsaction': 'JIbuQc:YxFE3d(IAcfIc),crCqv(kl0Ckd),sko5qc(vsmyDc);rcuQ6b:npT2md;GvneHb:GvneHb', 'jscontroller': 'glDwzc', 'class': 'GRaO7d'})
table = pdiv[0].contents[3]

#tContents = table.contents[3]
print() #for separation of outputs in terminal 
def getEPS():
    for tr in table:
        for td in tr:
            if (td.find(text=re.compile("Diluted EPS"))):
                output = td.text
                ratio = td.parent.find_all('td')[1].text
    return(output + ": " + ratio)
print(getEPS())
print()
def getNetIncome():
    NIrow = table.contents[2]
    NITitle = NIrow.find('div').text
    NetIncome = NIrow.contents[1].text
    NetGrowth = NIrow.contents[2].find('span').text
    print(NITitle + ": " + NetIncome)
    print(NetGrowth)
    NetGrowth = NetGrowth.replace('%', '')
    NetGrowth = float(NetGrowth)
    if (NetGrowth >= 20):
        return('Net Income Growth is good!')
    elif(NetGrowth >= 10):
        return('Net Income Growth is healthy, but could be better.')
    elif(NetGrowth >= 5):
        return('Net Income Growth is low.')
    elif(NetGrowth >= 0):
        return('Net Income Growth is not good.')
    else:
        return('Net Income Growth is negative. Not good at all!')
print(getNetIncome())
print()
def getPERatio():
    stockInfo = soup.find('div', {'class': "eYanAe", 'role': 'region', 'aria-labelledby': 'key-stats-heading'})
    stockInfo.find_all('div')
    infoRows = stockInfo.find_all('div', class_='gyFHrc')
    PErow = infoRows[5]
    PETitle = PErow.contents[0].contents[0].text
    PERatio = PErow.contents[1].text
    print(PETitle + ": " + PERatio)
    if (int(float(PERatio)) >= 20):
        return('P/E ratio is good!')
    else:
        return('P/E ratio is not good!')
print(getPERatio())
print()

def getDivYield():
    stockInfo = soup.find('div', {'class': "eYanAe", 'role': 'region', 'aria-labelledby': 'key-stats-heading'})
    stockInfo.find_all('div')
    infoRows = stockInfo.find_all('div', class_='gyFHrc')
    DivRow = infoRows[6]
    DivTitle = DivRow.contents[0].contents[0].text
    DivYield = DivRow.contents[1].text
    return(DivTitle + ": " + DivYield)
print(getDivYield())
print()

f = open("demofile.txt", "x")
f = open("demofile.txt", "a") # append
f.write(getEPS())
f.write(getNetIncome())
f.write(getPERatio())
f.write(getDivYield())
f.close()
#isPEGood
#20-25 is average
#if above and poor earnings -> not good!, overpriced
#if below and good earnings -> underpriced, good!

#isNetIncomeGood
#Margin of 5 is low, 10 is healthy, 20 or higher is good

#isEPSGood
#Higher the better
#Not a solid number, use it to compare against other stocks

#DivYield = infoRows[6]

#Changed to GOOGLE finance
#Wall Street Journal bans requests from webscrapers, Error 403
#much easier to look at, faster, webscraper friendly
#discovered more efficient and widespread indicators of a good stock
#EPS (earnings per share), P/E (price to earnings), PEG (price to earnings ratio to growth ratio), DPR (dividend payout ratio), dividend yield

#Objectives:
# -> Project Check #1
#Find EPS 
#Get P/E

#EPS = net profit/outstanding shares
#Amount each share would get if a company paid out all of its profit to its shareholders
#Indicates how profitable a company is -> direct relationship
#Steady EPS growth year after year is good (build feature in project check #2) -> find out what is a good growth

# -> Project Check #2
#Find PEG
#DPR
#Dividend Yield (could be #1?)
#Compare EPS to other companies to determine if its good or not