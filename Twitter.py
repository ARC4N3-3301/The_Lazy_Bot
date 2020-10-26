import tweepy

access_token = "MY_ACCESS_TOKEN" 
access_token_secret = "MY_ACCESS_TOKEN_SECRET"
consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"

def tweets(arg1, arg2):
	try:
		userID = arg1
		amt = int(arg2)
		text = []
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth)
		tweets = api.user_timeline(screen_name = userID,
            count = 100,
            include_rts = False, 
            tweet_mode = 'extended')
		for info in tweets[:amt]:
			text.append(info.full_text)
			#print("ID: {}".format(info.id))
            #date = info.created_at
		return text
	except:
		return False
