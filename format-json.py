import googlemaps
import json
from time import sleep

key = "AIzaSyCPUgKcJb0nY95u3hYqcvYxxuy4zW02Rh8"
client = googlemaps.client.Client(key)

tweets = []
for line in open('disease-data.json', 'r'):
	try:
		tweet_decoded = json.loads(line)
		tweets.append(tweet_decoded)
	except:
		print line

keywords = ['sick','#sick','#flu','#pneumonia','#disease', '#CDC', "runny nose", "fever", "aches", "cough", "fatigue", "runny nose", "#fever", "#aches", "#cough", "#fatigue", "cold", "headache", "#headache", '#flu', 'vomitting']

total_data_items = len(tweets)
counter = 0


formatted_data = []
for tweet in tweets:
	if counter == 700:
		break
	dictionary = dict()
	text = tweet['text']
	tweet_keywords = []
	for keyword in keywords:
		if keyword in text:
			tweet_keywords.append(keyword)
	if len(tweet_keywords) == 0:
		formatted_keywords = 'coughing'
	else:
		formatted_keywords = ','.join(tweet_keywords)
	date = tweet['created_at']
	place = tweet['place']['full_name']
	add = googlemaps.geocoding.geocode(client, place)[0]['geometry']['location']
	latitude = add['lat']
	longitude = add['lng']
	dictionary['lat'] = latitude
	dictionary['lng'] = longitude
	dictionary['date'] = date
	dictionary['keywords'] = formatted_keywords
	dictionary['tweetHandle'] = "@" + tweet['user']['screen_name']
	formatted_data.append(dictionary)
	counter += 1
	print(str(counter)  + " of " + str(total_data_items) + " tweets successfully parsed")

with open('illinois-final-json.json', 'w+') as file:
	json.dump(formatted_data, file, sort_keys=True, indent=4)
