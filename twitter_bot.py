import tweepy
from keys import *
from tweepy import Stream
import json
from datetime import date, datetime, timezone

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
client = tweepy.Client(bearer_token=BEARER)

keywords = [
{'word': 'pixelwar', 'phrase': 'Le pixelwar continue sur Paris, rdv sur kingofpaname.fr 🇫🇷'},
{'word': 'r/place', 'phrase': 'r/place continue sur Paris, rdv sur kingofpaname.fr 🇫🇷'},
{'word': '#pixelart', 'phrase': '👾 Viens faire du pixel art sur la carte de kingofpaname.fr 👾'},
{'word': 'strava ', 'phrase': '🏃‍♂️ Profite de ton jogging pour conquérir Paris sur kingofpaname.fr 👑'},
{'word': 'invaders', 'phrase': '👾 RDV sur kingofpaname.fr pour envahir la capitale 👾'},
{'word': ' velo ', 'phrase': '🚲 Profite de tes déplacements en vélo pour conquérir Paris sur kingofpaname.fr 👑'},
{'word': ' balade ', 'phrase': '🚶‍♀️ Profite de ta balade pour conquérir Paris sur kingofpaname.fr 👑'},
{'word': ' paname ', 'phrase': 'Tu parles de Paname ? RDV sur kingofpaname.fr pour conquérir la capitale 👑🇫🇷'}
]


status = True

class listener(tweepy.Stream):

  def on_data(self, data):
    global status
    today = date.today()
    dt = datetime.combine(date.today(), datetime.min.time()).astimezone().isoformat()
    count = client.get_users_tweets(id='1481967129457004548', start_time=dt).meta["result_count"] 
    # retrieve the bot's Twitter ID to count the daily amount of tweets

    all_data = json.loads(data)
    id_tweet = all_data["id_str"]
    tweet = all_data["text"]
    username = all_data["user"]["screen_name"]

    if username == 'tloizel':
    # enter your username

      if 'stop' in tweet.lower():

        print (today, ' - Bot off - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + 'Sad, turning bot off',
            in_reply_to_status_id=id_tweet
        )
        status = False
        return True

      elif 'start' in tweet.lower():

        print (today, ' - Bot on - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + 'Woohoo, turning bot back on',
            in_reply_to_status_id=id_tweet
        )
        status = True
        return True

    for x in keywords:

      if x['word'] in tweet.lower() and status == True and count < 10:
      # bot only tweets maximum 10 times a day to respect Twitter guidelines

        print (today, ' - ' + x['word'] + ' - ', username, tweet)
        api.update_status(
            status='@' + username + ' ' + x['phrase'],
            in_reply_to_status_id=id_tweet
        )
        break

      elif x['word'] in tweet.lower() and status == True and count >= 10:
        print (today, ' - @tloizel Turning off bot for today 💤')

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
          # use coordinates of the location you wish to filter (southwest longitude-latitude, northeast longitude-latitude)

        except:
            continue

start_stream()


