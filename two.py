from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetching_url():

	html = urlopen("http://shakespeare.mit.edu/lll/full.html")
	bsobj = BeautifulSoup(html.read(), "html.parser")
	print(bsobj)

fetching_url()