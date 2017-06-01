from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def fetching_url():
	html = urlopen("http://shakespeare.mit.edu/lll/full.html")
	bsobj = BeautifulSoup(html.read(), "html.parser")
	print(bsobj.h3)
	# step three
	# .get_text() strips all tags from the document you are working
	# with and returns a string containing the text only.
	# Calling  .get_text() should always be the last thing you do, immedi‐
	# ately before you print, store, or manipulate your final data.
 
	h3 = bsobj.findAll("h3")
	for tag in h3:
		print(tag.get_text())

	# step four
	nameList = bsobj.findAll(text="DUMAIN")
	# print(nameList)
	# print(len(nameList))

	new_object = bsobj.find("a",{"name":"1.1.9"})
	# print(new_object.get_text())

	new_object = bsobj.findAll("a",attrs={"name":re.compile(r"\d.\d.\d")})
	for tag in new_object:
		print(tag)














fetching_url()