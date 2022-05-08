import requests
from bs4 import BeautifulSoup 

url = "https://www.fandango.com/48116_movietimes?date=2022-03-11"

result = requests.get(url)

txt = BeautifulSoup(result.text, "html.parser")

# find all the "<li>" tags on the page
txt.find("li")
# Emagine Hartland theater id attr = "theater-aaymw"
print(txt.prettify())