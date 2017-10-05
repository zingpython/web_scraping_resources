from apiclient import discovery


API_KEY = ''
CSE_ID = ""

TMPL = '''
    Title: %s
    Snippet: %s
    URL: %s
'''
service = discovery.build("customsearch", "v1", developerKey=API_KEY)
res = service.cse().list(q="trump", cx=CSE_ID).execute().get('items', [])

# print(res)
for data in res:
    article = ' '.join(data['title'].strip().split())
    # print(type(data))
    if article:
        print(TMPL % (data['title'],
                      data['snippet'],
                      data['formattedUrl']))