import requests
from bs4 import BeautifulSoup

def fetching_url():
	html = requests.get("http://shakespeare.mit.edu/lll/full.html")
	print(html.status_code)
	bsobj = BeautifulSoup(html.content, "html.parser")
	print(bsobj.h3)

fetching_url()