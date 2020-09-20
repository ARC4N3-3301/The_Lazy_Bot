import tweepy
import discord 
from discord.ext import commands, tasks


access_token = "1140147595408363521-jqCaqgIkyE3bzSNfG2B73L1lLQj1CQ" 
access_token_secret = "n3Yj16QxBdCCZV22EW4NRJbyhBUZtnIbJPZdeUc9PFVAH"
consumer_key = "J7hw0EbEUV897bnWZLcSBXb9z"
consumer_secret = "LFe8PRnVVJ1gv9jQneWJO7L2NXSXZaULeyIh0Cwmirva5bGI1p"

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


def loop(arg):
	token = 'NzQxMzc0OTY4NjEyMjU3ODUy.Xy2pPg.R04bMQd6XQfoL0MEiEVA5ZQLUAM'
	something = commands.Bot("!")

	@tasks.loop(seconds = 15.0)
	async def called_once_a_day():
		text = tweets(arg,1)
		return (text[0])


	@called_once_a_day.before_loop
	async def before():
	    await something.wait_until_ready()

	called_once_a_day.start()

	something.run(token)