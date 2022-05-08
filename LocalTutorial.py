from bs4 import BeautifulSoup 

#how to access LOCAL html data
with open("index.html", "r") as file:
    doc = BeautifulSoup(file, "html.parser")

print(doc.prettify()) #print html 

tag = doc.title #gives access to the FIRST tag in the document
print(tag) #prints tag

print(tag.string) #how to access string inside of tag

tag.string = 'hello' #changes string to hello
print(tag.string)

tagf = doc.find_all("p") #finds all the p tags and the stuff inside them
tagf = doc.find_all("p")[0] #finds the first p tag

print(tagf.find_all("b")) #prints all the b tags and the stuff inside them

