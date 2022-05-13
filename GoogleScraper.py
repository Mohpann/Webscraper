import requests
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen
import re

class GoogleScraper:
    def __init__(self, ticker):
        self.ticker = ticker    
        self.url = f"https://www.google.com/finance/quote/{ticker}:NYSE?hl=en"
        self.req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})

        self.webpage = urlopen(self.req).read()
        self.soup = BeautifulSoup(self.webpage,'html.parser')

        self.pdiv = self.soup.find_all('div', {'jsaction': 'JIbuQc:YxFE3d(IAcfIc),crCqv(kl0Ckd),sko5qc(vsmyDc);rcuQ6b:npT2md;GvneHb:GvneHb', 'jscontroller': 'glDwzc', 'class': 'GRaO7d'})
        self.table = self.pdiv[0].contents[3]

    #tContents = table.contents[3]
    def getEPS(self):
        for tr in self.table:
            for td in tr:
                if (td.find(text=re.compile("Diluted EPS"))):
                    output = td.text
                    ratio = td.parent.find_all('td')[1].text
        return(output + ": " + ratio)

    def getNetIncome(self):
        NIrow = self.table.contents[2]
        NITitle = NIrow.find('div').text
        NetIncome = NIrow.contents[1].text
        NetGrowth = NIrow.contents[2].find('span').text
        print(NITitle + ": " + NetIncome)
        print(NetGrowth)
        NetGrowth = NetGrowth.replace('%', '')
        NetGrowth = float(NetGrowth)
        if (NetGrowth >= 20):
            return('Net Income Growth ' + '(' + str(NetGrowth) + '%' + ')' + " is good!")
        elif(NetGrowth >= 10):
            return('Net Income Growth ' + '(' + str(NetGrowth) + '%' + ')' + " is healthy, but could be better.")
        elif(NetGrowth >= 5):
            return('Net Income Growth ' + '(' + str(NetGrowth) + '%' + ')' + ' is low.')
        elif(NetGrowth >= 0):
            return('Net Income Growth '  + '(' + str(NetGrowth) + '%' + ')' + ' is not good.')
        else:
            return('Net Income Growth ' + '(' + str(NetGrowth) + '%' + ')' + ' is negative. Not good at all!')

    def getPERatio(self):
        stockInfo = self.soup.find('div', {'class': "eYanAe", 'role': 'region', 'aria-labelledby': 'key-stats-heading'})
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


    def getDivYield(self):
        stockInfo = self.soup.find('div', {'class': "eYanAe", 'role': 'region', 'aria-labelledby': 'key-stats-heading'})
        stockInfo.find_all('div')
        infoRows = stockInfo.find_all('div', class_='gyFHrc')
        DivRow = infoRows[6]
        DivTitle = DivRow.contents[0].contents[0].text
        DivYield = DivRow.contents[1].text
        return(DivTitle + ": " + DivYield)

    def getRevenue(self):
        revRow = self.table.contents[1]
        revTitle = revRow.find('div').text
        revenue = revRow.contents[1].text
        revenueGrowth = revRow.contents[2].find('span').text
        print(revTitle + ": " + revenue)
        print(revenueGrowth)
        revenueGrowth = revenueGrowth.replace('%', '')
        revenueGrowth = float(revenueGrowth)
        if (revenueGrowth >= 20):
            return('Revenue Growth ' + '(' + str(revenueGrowth) + '%' + ')' + " is good!")
        elif(revenueGrowth >= 10):
            return('Revenue Growth' + '(' + str(revenueGrowth) + ')' + '%' + ' is healthy, but could be better.')
        elif(revenueGrowth >= 5):
            return('Revenue Growth is' + '(' + str(revenueGrowth) + '%' + ')' + ' low.')
        elif(revenueGrowth >= 0):
            return('Revenue Growth' + '(' + str(revenueGrowth) + '%' + ')' + ' is not good.')
        else:
            return('Revenue Growth' + '(' + str(revenueGrowth) + '%' + ')' + 'is negative. Not good at all!')