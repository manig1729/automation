#! python3

# This code selects a random song from an Excel sheet (Song_list.xlsx)
# And sends out a tweet from my twitter account recommending that song

import tweepy
import openpyxl
import random

# You can get the following keys using the Twitter API
# Apply on developer.twitter.com and create a new app
# Note - the API must have read and write permissions to tweet on your behalf

consumer_key = '<Your consumer key here>'
consumer_secret = '<Your consumer secret key here>'

access_token = '<Your access token here>'
access_token_secret = '<Your access token secret here>'

wb = openpyxl.load_workbook('Song_list.xlsx')
sheet = wb['Sheet1']
num = random.randint(2, 181)

song = 'A' + str(num)
artist = 'B' + str(num)

twt = "Hello Twitter! Here's a song for you. Check out - "+ sheet[song].value + " by " + sheet[artist].value

def OAuth():
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		return auth
	except Exception as e:
		return None

oauth = OAuth()
api = tweepy.API(oauth)

api.update_status(twt)
