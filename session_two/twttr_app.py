import twitter
import json

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
						   CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

# first
# we get a twitter object
# print(twitter_api)

# second 
# lets get news based on location
WORLD_WOE_ID = 1
US_WOE_ID = 23424977
# prefix ID with the underscore for query string parameterization.
# without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.
world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
# print("US Trends",us_trends)
# lets conver twitter object to string, dumps takes an object and produces a string 

# print(json.dumps(us_trends, indent=1))
# from this we can get trends 
world_trends_set = set([trend['name']for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name']for trend in us_trends[0]['trends']])

# print(us_trends_set)

# third
# lets see if trends intersect 
common_trends = world_trends_set.intersection(us_trends_set)

# print("Common trends",common_trends)

# fourth
# lets pic a trend and exemine it further
q = '#5HDOWN'
count = 100
search_results = twitter_api.search.tweets(q=q, count=count)
# print(type(search_results))
statuses = search_results['statuses']
# print(statuses)

# five
# now we can iteriate statuses
status_texts = [ status['text'] for status in statuses ]
screen_names = [ user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions'] ]
hashtags = [ hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags'] ]

# print(status_texts)
# print(screen_names)


# Serialize obj to a JSON formatted str
# print(json.dumps(status_texts[0:5], indent=1))
# l = json.dumps(status_texts[0:5], indent=1)
# print(type(l))
print(json.dumps(status_texts[0:5], indent=1))
# print(json.dumps(screen_names[0:5], indent=1))
# print(json.dumps(hashtags[0:5], indent=1))
# print(json.dumps(words[0:5], indent=1))
# Compute a collection of all words from all tweets
words = [ w for t in status_texts for w in t.split() ]
print("Printing Words",words)













