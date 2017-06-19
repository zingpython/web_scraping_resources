import twitter
import json
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
						   CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
# print(twitter_api)
WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
# print("US Trends",us_trends)
world_trends_set = set([trend['name']for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name']for trend in us_trends[0]['trends']])
# print(us_trends_set)
common_trends = world_trends_set.intersection(us_trends_set)
# print("Common trends",common_trends)
#StarTrekDiscovery
q = '#StarTrekDiscovery'
count = 100
search_results = twitter_api.search.tweets(q=q, count=count)
# print(type(search_results))
statuses = search_results['statuses']
# print(statuses)
status_texts = [ status['text'] for status in statuses ]
screen_names = [ user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions'] ]
hashtags = [ hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags'] ]
# print(status_texts)
print(json.dumps(status_texts[0:5], indent=1))

















