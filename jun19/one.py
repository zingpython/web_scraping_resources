import requests
from bs4 import BeautifulSoup

def fetching_url():
	url = u'https://twitter.com/search?q='
	# query = u'%40zingpython'
	# query = u'%32'
	query = u'trump'
	html = requests.get(url+query)
	print(html.status_code)
	bsobj = BeautifulSoup(html.text, 'html.parser')
	tweets = [p.text for p in bsobj.findAll('p', class_='tweet-text')]
	print(tweets)

fetching_url()