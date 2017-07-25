from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def fetching_url():

	html = urlopen("http://programwithus.com/events/")
	bsobj = BeautifulSoup(html.read(), "html.parser")
	# print(bsobj)
	emails = bsobj.findAll(text=re.compile(r"[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)"))
	print(emails)


fetching_url()