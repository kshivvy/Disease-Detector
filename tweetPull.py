import tweepy
import datetime
import jsonpickle

CONSUMER_KEY = "SFcxwLBVF4YmVERD8YbFAbHVR"
CONSUMER_SECRET = "bAjMKe6BeEIQ9lH3JzJsJsRTRjkHQg9hHRgEB42Xdbjqfxv6Fz"
access_token = "717755279488782336-w9RE9xptHI5rPFflQf4qy47ofqsJitO"
access_token_secret = "WgVxnf7ZaYPDqsPygjK6FCGwo9pw9w4nKdQeaoLAl6j85"


# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(access_token, access_token_secret)

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

query = "disease exclude:retweets"
max_tweets = 5000
start_date = ""
end_date = ""
chicago_place_id = "1d9a5370a355ab0c"
champaign_place_id = "2335250557ea3fb4"
search_query = "place:f54a2170ff4b15f7 #sick OR sick OR #cough OR cough OR #fever OR fever OR #aches OR aches OR #fatigue OR fatigue OR #flu OR #pneumonia OR #disease OR #CDC OR headache OR dizziness OR nausea OR fatigue OR fever OR vomitting"

# places = api.geo_search(query="Illinois", granularity="city")
# print(places[0].id)

tweetCount = 0

with open('disease-data.json', 'w+') as f:
    for tweet in tweepy.Cursor(api.search,q=search_query).items(10000) :         
        if tweet.place is not None:
            
            #Write the JSON format to the text file, and add one to the number of tweets we've collected
            f.write(jsonpickle.encode(tweet._json, unpicklable=True) + '\n')
            tweetCount += 1
        else:
        	print "x"

    #Display how many tweets we have collected
    print("Downloaded {0} tweets".format(tweetCount))