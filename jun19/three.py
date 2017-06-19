from apiclient import discovery

TMPL = '''
    User: %s
    Date: %s
    Post: %s
'''
API_KEY = ''
GPLUS = discovery.build('plus', 'v1', developerKey=API_KEY)
items = GPLUS.activities().search(query='trump').execute().get('items', [])
print(items)

for data in items:
    post = ' '.join(data['title'].strip().split())
    if post:
        print(TMPL % (data['actor']['displayName'],
                      data['published'], post))