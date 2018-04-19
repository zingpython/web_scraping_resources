from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetching_url():

	html = urlopen("http://shakespeare.mit.edu/lll/full.html")
	bsobj = BeautifulSoup(html.read(), "html.parser")
	# step one
	print(bsobj)
	# # step two
	print(bsobj.h3)

	# # step three
	# # .get_text() strips all tags from the document you are working
	# # with and returns a string containing the text only.
	# # Calling  .get_text() should always be the last thing you do, immedi‐
	# # ately before you print, store, or manipulate your final data.
 
	h3 = bsobj.findAll("h3")
	for tag in h3:
		print(tag.get_text())



	# step four
	nameList = bsobj.findAll(text="DUMAIN")
	print(nameList)
	print(len(nameList))

	# # step four
	new_object = bsobj.find("a",{"name":"1.1.9"})
	print(new_object.get_text())

	allTags = bsobj.findAll('h3',limit=2)
	for t in allTags:
		print(t)

	# allTags = bsobj.findAll(True)
	# for t in allTags:
	# 	print(t.name)
	# 	print(t.h3)

fetching_url()