from bs4 import BeautifulSoup
import requests

#with open('index.html', 'r') as f:
#    doc = BeautifulSoup(f, 'html.parser')
#tags = doc.find_all("p")
#print(tags.string)

url = "https://www.scrapethissite.com/pages/"

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

header = doc.find_all ("h1")
Parent = header[0].parent
print(Parent)

