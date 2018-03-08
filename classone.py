import requests
from bs4 import BeautifulSoup
import csv

symbols = ['SPY','XLY','XLP']

url = "https://finance.yahoo.com/quote/"
page = "/profile"

csvFile = open("ETF.csv", 'a')
writer = csv.writer(csvFile)

header = [['Category','Fund Family','Net Assets','YTD Return','Yield','Legal Type']]
writer.writerows(header)

for s in symbols:
    greatList = []
    html = requests.get(url+s+page)
    bsobj = BeautifulSoup(html.content, "html.parser")
#     print(bsobj)
    text = bsobj.find('div', {'class':'Lh(21px)'})
    text = text.get_text()
#     print(text)
    data = bsobj.find('div', {'data-reactid':'24'})
    data = data.findAll('span', {'class':'Fl(end)'})
    # print(data)
    for line in data:
        greatList.append(line.get_text())
    print(greatList)
    writer.writerow(greatList)