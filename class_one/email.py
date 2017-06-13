import requests
from bs4 import BeautifulSoup

def fetching_url():
	html = requests.get("http://clickaces.com/contact/")
	# print(html.status_code)
	bsobj = BeautifulSoup(html.content, "html.parser")
	print(bsobj)


fetching_url()