import tweepy as tp  # pip install tweepy

auth = tp.OAuthHandler("petU9I2MLe9koGOcikP8DN2WS", "cBVqJTcDTpk0F6OCqL7G8px2dgniYVPbEuvVXDMQVK8LWk6BlJ")
auth.set_access_token("1267671961846439938-nMzYeeMo49SRMC0JUV2kdlLAPMpFwV", "5S4w4f7mM7LoGANKZFkLkQAo284TaxDt4z88LHca3rCTM")

api = tp.API(auth)

user = api.get_user('@elonmusk')
timeline = api.user_timeline('@elonmusk', trim_user=True, exclude_replies=True)

for tweet in timeline:
    text = tweet.text.lower()
    if 'snl' not in text:
        print('buy dogecoin $50')
    elif 'dogecoin' in text:
        print('buy dogecoin $100')
    print('test')