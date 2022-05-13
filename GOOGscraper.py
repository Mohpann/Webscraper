import requests
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen
import re
import GoogleScraper #OR from MODULE GoogleScraper import CLASS GoogleScraper

#import GoogleScraper imports the WHOLE file, you want to import the class WITHIN the file

#https://investoracademy.org/top-10-fundamental-analysis-indicators-for-all-investors/ -> good fundamental analysis indicators
#https://www.getsmarteraboutmoney.ca/invest/investment-products/stocks/6-indicators-used-to-assess-stocks/ -> same thing but with formulas

#tContents = table.contents[3]
print() #for separation of outputs in terminal 
ticker = "ORCL"
scraper = GoogleScraper.GoogleScraper(ticker)
print(scraper.getEPS())
print()

print(scraper.getNetIncome())
print()

print(scraper.getPERatio())
print()

print(scraper.getDivYield())
print()

f = open("demofile.txt", "x")
f = open("demofile.txt", "a") # append
f.write(scraper.getEPS())
f.write("\n")
f.write(scraper.getRevenue())
f.write("\n")
f.write(scraper.getNetIncome())
f.write("\n")
f.write(scraper.getPERatio())
f.write("\n")
f.write(scraper.getDivYield())
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
#Dividend Yield (could be #1?)
#Compare EPS to other companies to determine if its good or not