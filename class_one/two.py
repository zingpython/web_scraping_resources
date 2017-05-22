import requests
from bs4 import BeautifulSoup

def fetching_url():
	html = requests.get("http://shakespeare.mit.edu/lll/full.html")
	print(html.status_code)
	bsobj = BeautifulSoup(html.content)
	print(bsobj)

fetching_url()