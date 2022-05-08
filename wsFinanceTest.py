import os
import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
import selenium
import time

driver = webdriver.Chrome()
ticker = "ORCL"
url = f"https://finance.yahoo.com/quote/{ticker}/balance-sheet?p={ticker}"
result = requests.get(url)
soup = BeautifulSoup(result.text,'html.parser')

totalAssetsButton = driver.find_element_by_name('P(0) M(0) Va(m) Bd(0) Fz(s) Mend(2px) tgglBtn')
totalAssetsButton.click()

currAssets = soup.findAll('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')

print(currAssets)

 