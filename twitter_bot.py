import tweepy
from keys import *
from tweepy import Stream
import json


text = ('RDV sur kingofpaname pour conquérir la capitale 👑🇫🇷')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

class listener(tweepy.Stream):

    def on_data(self, data):
      all_data = json.loads(data)
      id_tweet = all_data["id_str"]
      tweet = all_data["text"]
      username = all_data["user"]["screen_name"]

      if 'panameyyyk' in tweet.lower():

        print (username, tweet)
        api.update_status(
            status='@' + username + ' ' + text,
            in_reply_to_status_id=id_tweet
        )

        return True

    def on_error(self, status):
        print(status)


twtr_stream = listener(
  CONSUMER_KEY, CONSUMER_SECRET,
  ACCESS_KEY, ACCESS_SECRET
)

twtr_stream.filter(locations=[2.243856,48.812425,2.428220,48.904584])

# twtr_stream.filter(languages=["fr"], locations=[2.243856,48.812425,2.428220,48.904584])


# search for paname only in tweet not name && in Paris
# reply
#id for Paris 09f6a7707f18e0b1 (https://api.twitter.com/1.1/geo/reverse_geocode.json?lat=48.864716&long=2.349014)
# place:09f6a7707f18e0b1
# lang:fr
# paname place:09f6a7707f18e0b1 lang:fr

