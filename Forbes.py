import requests
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen
import re

url = f"https://www.forbes.com/real-time-billionaires/#79e910c43d78"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')

richestperson = soup.find('a', {"ng-href": "https://www.forbes.com/profile/elon-musk/?list=rtb/"})
print(richestperson.text)