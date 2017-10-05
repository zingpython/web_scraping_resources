from apiclient import discovery

API_KEY = 'AIzaSyA7RZEzUkOR7L6MLqxrqMgCN0pbrqFEFdE'

GPLUS = discovery.build('plus', 'v1', developerKey=API_KEY)
items = GPLUS.activities().search(query='trump').execute().get('items', [])

print(items)