from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import sqlite3

conn = sqlite3.connect('seven.db')
c = conn.cursor()


# first create db schema
def create_db():
	c.execute('''CREATE TABLE 'sp' (
				'id' INTEGER,
				'month' VARCHAR,
				'last' VARCHAR,
				'change' VARCHAR,
				'prior_settle' VARCHAR,
				'open'	VARCHAR,
				'high' VARCHAR,
				'low' VARCHAR,
				'volume' VARCHAR,
				'hi_low_limit' VARCHAR,
				'updated'VARCHAR,
				PRIMARY KEY ('id')
		)''')


	conn.commit()
create_db()



# second get and check data
# def get_data():

# 	req = Request('http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html', headers={'User-Agent': 'Mozilla/5.0'})
# 	webpage = urlopen(req).read()
# 	bsobj = BeautifulSoup(webpage, "html.parser")
# 	table = bsobj.find("table",{"id":"quotesFuturesProductTable1"})

# 	list_of_lists =[]

# 	rows = table.findAll("tr")
# 	for row in rows:
# 		listRow = []
# 		for cell in row.findAll(['td','th']):
# 			listRow.append(cell.get_text())
# 		list_of_lists.append(listRow)
# 	return list_of_lists


		
# check data with print		
# def insert_data_in_db():
# 	data = get_data()
# 	# print(data)		
		
	

# 	for month, _, _, last, change, prior_settle, _open, high, low, volume, low_high, updated in data[2::]:
# 		# print(month, _, _, last, change, prior_settle, _open, high, low, volume, low_high, updated)
# 		new_data = (month,last, change, prior_settle, _open, high, low, volume, low_high, updated)
# 		print(new_data)
# 		c.execute('INSERT INTO sp(month,last, change, prior_settle, open, high, low, volume, hi_low_limit, updated) VALUES(?,?,?,?,?,?,?,?,?,?)', new_data)
# 		conn.commit()
# 	conn.close()

# insert_data_in_db()