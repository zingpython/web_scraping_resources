import requests
from bs4 import BeautifulSoup

def fetching_url():
	html = requests.get("http://shakespeare.mit.edu/lll/full.html")
	print(html.status_code)
	bsobj = BeautifulSoup(html.content, "html.parser")
	# print(bsobj.h3)

	# h3 = bsobj.findAll("h3")
	# for tag in h3:
	# 	print(tag.get_text())

	nameList = bsobj.findAll(text="DUMAIN")
	print(nameList)
	print(len(nameList))

	new_object = bsobj.find("a",{"name":"1.1.9"})
	print(new_object.get_text())

fetching_url()