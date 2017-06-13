import requests
from bs4 import BeautifulSoup
import re

def fetching_url():
	html = requests.get("http://clickaces.com/contact/")
	# print(html.status_code)
	bsobj = BeautifulSoup(html.content, "html.parser")
	# print(bsobj)
	emails = bsobj.findAll(text=re.compile(r"[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)"))
	print(emails)

fetching_url()