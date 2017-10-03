from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv
# Header cells - contains header information (created with the <th> element)
# Standard cells - contains data (created with the <td> element)

def table_to_csv():
	req = Request('http://www.cmegroup.com/trading/'\
		'equity-index/us-index/e-mini-sandp500.html', \
		headers={'User-Agent': 'Mozilla/5.0'})

	# req = Request("http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500_quotes_settlements_futures.html",headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	bsobj = BeautifulSoup(webpage, "html.parser")
	# print(bsobj)
	table = bsobj.find("table",{"id":"quotesFuturesProductTable1"})
	# # table = bsobj.find("table",{"id":"settlementsFuturesProductTable"})
	# print(table)

	# # step three

	csvFile = open("sp_h.csv", 'wt')
	writer = csv.writer(csvFile)


	# # # step two
	rows = table.findAll("tr")
	# print(rows)

	for row in rows:
	# # 	# print(row)
		csvRow = []
		for cell in row.findAll(['td','th']):
	# 		# print(cell)
			csvRow.append(cell.get_text())
		print(csvRow)

		writer.writerow(csvRow)




table_to_csv()