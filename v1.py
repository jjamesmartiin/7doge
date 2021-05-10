import time
import tweepy as tp  # pip install tweepy
import re  # pip install regex
# from webull import webull
from webull import paper_webull # pip install webull 

def authorize():
    auth = tp.OAuthHandler("petU9I2MLe9koGOcikP8DN2WS", "cBVqJTcDTpk0F6OCqL7G8px2dgniYVPbEuvVXDMQVK8LWk6BlJ")
    auth.set_access_token("1267671961846439938-nMzYeeMo49SRMC0JUV2kdlLAPMpFwV", "5S4w4f7mM7LoGANKZFkLkQAo284TaxDt4z88LHca3rCTM")
    authorize.api = tp.API(auth)

doge = "doge"
dogecoin = "dogecoin"

def get_latest_tweet(twitter_handle):
    get_latest_tweet.timeline = authorize.api.user_timeline(twitter_handle, count=1, trim_user=False, exclude_replies=True)
    # tweet will fail if the user does not exist, implement try block soon

# while True:
authorize()
get_latest_tweet('elonmusk')
for tweet in get_latest_tweet.timeline:
    text = tweet.text.lower()
    print(text)
    if re.search(dogecoin, text):
        print('buy dogecoin $100')
    elif re.search(doge, text):
        print(' buy dogecoin $50')
# time.sleep(1)

# webull section
wb = paper_webull()
wb.login('jjamesmartiin@gmail.com', '9hyur^8Q3tZp')

wb.get_trade_token('719656')
wb.place_order(stock='DOGEUSD', price=)