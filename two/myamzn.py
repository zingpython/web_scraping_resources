import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

asin_list = ['B002EYASY8','B074HL9TL8',]


def get_data():
	headers = {'User-Agent': 'Mozilla/5.0'}

	csvFile = open("amzn.csv", 'wt')
	writer = csv.writer(csvFile)

	for i in asin_list:
		csvRow = []
		url = "http://www.amazon.com/dp/"+i
		print ("Processing: "+url)
		page = requests.get(url,headers=headers)
		# print(page)
		bsobj = BeautifulSoup(page.content, "html.parser")
		product = bsobj.find("span",{"id":"productTitle"})
		# print(product)
		price = bsobj.find("span",{"id":"priceblock_ourprice"})
		print(price)
		price = price.get_text().replace("$"," ")
		all_bullets = bsobj.find("div", {"id":"feature-bullets"})
		# print(all_bullets)
		product = ' '.join([i.strip() for i in product])
		# print("New product", product) 

		also_viewed = bsobj.findAll("span",class_="p13n-sc-price")
		also_viewed = [item.get_text().replace("$"," ") for item in also_viewed]
		# print(also_viewed)
		##################list comp example #############
		# lowest_price_new = []
		# for var in also_viewed:
		# 	print("Var :6",var[:6])
		# 	lowest_price_new.append(float(var))
		# 	print("New Lowest", lowest_price_new)
		# 	print("MIN",min(lowest_price_new))
		################################################

		lowest_price = min([float(price[:6]) for price in also_viewed])
		if float(price[:6]) < lowest_price:
			message = "This is a lowest price"
		else:
			lesspercent = float(price[:6])/lowest_price
			# print(lesspercent)
			message = "Lowest price in this category: "+str(lowest_price)
		csvRow.extend((product,price,message))
		for bullet in all_bullets.findAll("li"):
			# print(bullet.get_text())
			csvRow.append(bullet.get_text().strip())
		print(csvRow)
		writer.writerow(csvRow)
get_data()
	



	