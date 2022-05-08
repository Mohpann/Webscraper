#how to access online HTML data
import requests

from bs4 import BeautifulSoup 

url = "https://tarkov-market.com/"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.findAll("div")[0]
print(prices.prettify())

#tags within a tag are called descendants, and descendants have parents
#.find(str) give the FIRST result
#.findAll(str) gives all the results