import tweepy
from time import sleep
import json
# from tweepy.parsers import JSONParser

CONSUMER_KEY = 'Q88u0KvQK4f7fGfqO43SxVbcE'
CONSUMER_SECRET = 'ahQk6VKzjuF5eucS6a6DJT3LubBqnBTj5JxT2BvBTaIDMKkZhO'
OAUTH_TOKEN = '797271725629173762-0Y2XBwZGwjfcTpXLGLxZCKOI3mDmEtq'
OAUTH_TOKEN_SECRET = 'tdVlX8T6NZzoOiEpG6f7oAUrMRwOK765sITdzWgbhjRZo'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)


# # For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search,q='Trump').items(50):
    t = json.dumps(tweet)
    print(t["text"])


# Print out usernames of the last 10 people to use #ocean
    # print('Tweet by: @' + tweet.user.screen_name)
    # print(tweet.text)

# Open text file verne.txt (or your chosen file) for reading
# my_file = open('mytext.txt', 'r')

# # Read lines one by one from my_file and assign to file_lines variable
# file_lines = my_file.readlines()

# # Close file
# # my_file.close()

# # for line in file_lines:
# # # Add try ... except block to catch and output errors
# #     try:
# #         print(line)
# #         if line != '\n':
# #             api.update_status(line)
# #         else:
# #             pass
# #     except tweepy.TweepError as e:
# #         print(e.reason)
# #     sleep(5)

# # Tweet a line every 15 minutes
# def tweet():
#     for line in file_lines:
#         try:
#              print(line)
#              if line != '\n':
#                  api.update_status(line)
#                  sleep(900)
#              else:
#                 pass
#         except tweepy.TweepError as e:
#             print(e.reason)
#             sleep(2)

# tweet()









