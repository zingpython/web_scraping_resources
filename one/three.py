import requests
from bs4 import BeautifulSoup

html = requests.get("https://finance.yahoo.com/quote/SPY/profile?p=SPY")
bsobj = BeautifulSoup(html.content, "html.parser")
# print(bsobj)
phone = bsobj.find('span', {'class':"D(b) Lh(21px) Mb(20px) C($c-fuji-blue-1-b)"})
phone.get_text()

data = bsobj.find('div', {'data-reactid':'24'})
data = data.findAll('span', {'class':'Fl(end)'})

for i in data:
    print(i.get_text())

text = bsobj.find('div', {'class':'Lh(21px)'})
text.get_text()


