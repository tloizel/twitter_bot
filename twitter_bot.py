import tweepy
from keys import *
from tweepy import Stream
import json


text1 = ('Tu parles de Paname ? RDV sur kingofpaname pour conquérir la capitale 👑🇫🇷')
text2 = ('👾 RDV sur kingofpaname pour envahir la capitale 👾')
text3 = ('🏃‍♂️ Profite de ton jogging pour conquérir Paris 👑')
text4 = ('🚶‍♀️ Profite de ta balade pour conquérir Paris 👑')
text5 = ('🚲 Profite de tes déplacements en vélo pour conquérir Paris 👑')
text6 = ('Tu parles de Paris ? RDV sur kingofpaname pour conquérir la capitale 👑🇫🇷')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

class listener(tweepy.Stream):

    def on_data(self, data):
      all_data = json.loads(data)
      id_tweet = all_data["id_str"]
      tweet = all_data["text"]
      username = all_data["user"]["screen_name"]

      if 'paname' in tweet.lower():

        print ('Paname - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + text1,
            in_reply_to_status_id=id_tweet
        )

      elif 'invaders' in tweet.lower():

        print ('Invaders - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + text2,
            in_reply_to_status_id=id_tweet
        )

      elif 'strava' in tweet.lower():

        print ('Strava - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + text3,
            in_reply_to_status_id=id_tweet
        )

      elif 'balade' in tweet.lower():

        print ('Balade - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + text4,
            in_reply_to_status_id=id_tweet
        )

      elif 'velo' in tweet.lower():

        print ('Velo - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + text5,
            in_reply_to_status_id=id_tweet
        )

      elif 'paris' in tweet.lower():

        print ('Paris - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + text6,
            in_reply_to_status_id=id_tweet
        )

      return True

    def on_error(self, status):
        print(status)


def start_stream():
    while True:
        try:
          twtr_stream = listener(
            CONSUMER_KEY, CONSUMER_SECRET,
            ACCESS_KEY, ACCESS_SECRET
          )
          twtr_stream.filter(locations=[2.243856,48.812425,2.428220,48.904584])
        except:
            continue

start_stream()

# twtr_stream.filter(languages=["fr"], locations=[2.243856,48.812425,2.428220,48.904584])


# search for paname only in tweet not name && in Paris
# reply
#id for Paris 09f6a7707f18e0b1 (https://api.twitter.com/1.1/geo/reverse_geocode.json?lat=48.864716&long=2.349014)
# place:09f6a7707f18e0b1
# lang:fr
# paname place:09f6a7707f18e0b1 lang:fr

