import requests
from bs4 import BeautifulSoup
import csv

asin_list = ['B002EYASY8','B074HL9TL8']

headers = {'User-Agent': 'Mozilla/5.0'}

csvFile = open("amzn.csv", 'wt')
writer = csv.writer(csvFile)

for i in asin_list:
	csvRow = []
	url = "http://www.amazon.com/dp/"+i
	print ("Processing: "+url)
	page = requests.get(url,headers=headers)
	bsobj = BeautifulSoup(page.content, "html.parser")
	# print(bsobj)
	product = bsobj.find("span",{"id":"productTitle"})
	price = bsobj.find("span",{"id":"priceblock_ourprice"})
	# print(price)
	all_bullets = bsobj.find("div", {"id":"feature-bullets"})
	price = price.get_text().replace("$"," ")
	product = ' '.join([i.strip() for i in product])
	also_viewed = bsobj.findAll("span",class_="p13n-sc-price")
	also_viewed = [item.get_text().replace("$"," ") for item in also_viewed]
	print(price)
	lowest_price = min([float(price[:6]) for price in also_viewed])
	print(lowest_price)
	if float(price[:6]) < lowest_price:
		message = "This is a lowest price"
	else:
		# lesspercent = float(price[:6])/lowest_price
		# print(lesspercent)
		message = "Lowest price in this category: "+str(lowest_price)
	csvRow.extend((product,price,message))
	for bullet in all_bullets.findAll("li"):
		csvRow.append(bullet.get_text().strip())
	print(csvRow)
	writer.writerow(csvRow)
















