import requests
from bs4 import BeautifulSoup

def fetching_url():
	html = requests.get("http://shakespeare.mit.edu/lll/full.html")
	bsobj = BeautifulSoup(html.content, "html.parser")

fetching_url()