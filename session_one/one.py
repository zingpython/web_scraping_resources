import requests
from bs4 import BeautifulSoup
import re

def fetching_url():

	html = requests.get("http://shakespeare.mit.edu/lll/full.html")
	bsobj = BeautifulSoup(html.content, "html.parser")
	# print(bsobj)

	# h3 = bsobj.findAll("h3")
	# print(h3)
	# for tag in h3:
	# 	print(tag.get_text())

	new_object = bsobj.findAll("a",attrs={"name":re.compile(r"\d.\d.\d")})
	for tag in new_object:
		print(tag)


fetching_url()