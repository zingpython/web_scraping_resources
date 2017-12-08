import requests
from bs4 import BeautifulSoup

html = requests.get("http://shakespeare.mit.edu/lll/full.html")
bsobj = BeautifulSoup(html.content, "html.parser")
print(bsobj)