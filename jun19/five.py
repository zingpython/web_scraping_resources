import sqlite3 as sq3

#creating database
conn = sq3.connect('four.db')
c = conn.cursor()
query = 'CREATE TABLE stock (symbol, price)'
# c.execute(query)
# conn.commit()

#inserting values
c.execute("INSERT INTO stock VALUES(?,?)", ("AAPL", "119"))
conn.commit()