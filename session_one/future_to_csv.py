from bs4 import BeautifulSoup
import requests
# from urllib.request import Request, urlopen
import csv

def table_to_csv():
	html = requests.get('http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html', headers={'User-Agent': 'Mozilla/5.0'})
	# context=context
	# webpage = urlopen(req).read()
	bsobj = BeautifulSoup(html.content, "html.parser")
	# print(bsobj)

	table = bsobj.find("table",{"id":"quotesFuturesProductTable1"})
	# print(table)
	rows = table.findAll("tr")
	print(rows)

	csvFile = open("sp_h.csv", 'wt')
	writer = csv.writer(csvFile)

	for row in rows:
		# print(row)
		csvRow = []
		for cell in row.findAll(['td','th']):
			# print(cell)
			csvRow.append(cell.get_text())
		# print(csvRow)
		writer.writerow(csvRow)


table_to_csv()
# import ssl
# context = ssl._create_unverified_context()
# context=context