import tweepy
from keys import *
from tweepy import Stream
import json

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

keywords = [
{'word': 'strava', 'phrase': '🏃‍♂️ Profite de ton jogging pour conquérir Paris 👑'},
{'word': 'invaders', 'phrase': '👾 RDV sur kingofpaname pour envahir la capitale 👾'},
{'word': 'velo', 'phrase': '🚲 Profite de tes déplacements en vélo pour conquérir Paris 👑'},
{'word': 'balade', 'phrase': '🚶‍♀️ Profite de ta balade pour conquérir Paris 👑'},
{'word': 'paname', 'phrase': 'Tu parles de Paname ? RDV sur kingofpaname pour conquérir la capitale 👑🇫🇷'}
]

status = True

class listener(tweepy.Stream):

  def on_data(self, data):
    global status
    all_data = json.loads(data)
    id_tweet = all_data["id_str"]
    tweet = all_data["text"]
    username = all_data["user"]["screen_name"]

    if username == 'tloizel':

      if 'stop' in tweet.lower():

        print ('Bot off - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + 'Sad, turning bot off',
            in_reply_to_status_id=id_tweet
        )
        status = False
        return True

      elif 'start' in tweet.lower():

        print ('Bot on - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + 'Woohoo, turning bot back on',
            in_reply_to_status_id=id_tweet
        )
        status = True
        return True

    for x in keywords:

      if x['word'] in tweet.lower() and status == True:

        print (x['word'] + ' - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + x['phrase'],
            in_reply_to_status_id=id_tweet
        )
        break

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


