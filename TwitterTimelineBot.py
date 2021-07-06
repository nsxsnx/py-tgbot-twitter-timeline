#!/usr/bin/python3
import time, pickle, urllib.request, urllib.error, json
from urllib.parse import quote
from twython import Twython, TwythonError
from SETTINGS import *

def send_message(pmsg):
    msg = quote(pmsg.encode('utf8'), safe='')
    link = TG_LINK.format(TOKEN = TELEGRAM_TOKEN, CHANNEL = TELEGRAM_CHANNEL, MESSAGE = msg)
    res = json.loads(str(urllib.request.urlopen(link).read(), 'utf-8'))
    if not res['ok']: raise urllib.error.HTTPError
   
def prettyprint(data):
    for k, v in data.items(): print(k, ' ---> ', v)

def kill_unsupported_tags(s):
    for t in UNSUPPORTED_TAGS: s = s.replace(t, '')
    return s

def die(message):
    print(message)
    exit(1)

# Entry point
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try: tweet_id = pickle.load(open(STATE_FILE, "rb"))
except: # First run
    try:
        tweets = twitter.get_home_timeline(screen_name=TWITTER_USER_NAME, count=10, tweet_mode='extended')
        tweet_id = tweets[-1]['id']
    except TwythonError as e:
        print(e)
        die("Can't get home timeline")
    with open(STATE_FILE, "wb") as fw: pickle.dump(tweet_id, fw)
    print("STATE_FILE created with tweet_id ", tweet_id)
    exit(0)
if not tweet_id: exit(1)
try: tweets = twitter.get_home_timeline(screen_name=TWITTER_USER_NAME, since_id=tweet_id, tweet_mode='extended')
except TwythonError as e:
    print(e)
    die("Can't get home timeline")
for t in reversed(tweets):
    #prettyprint(t)
    if t['user']['verified']: name = '✅' + t['user']['name']
    else: name = '❔' + t['user']['name']
    txt = Twython.html_for_tweet(t)
    txt = kill_unsupported_tags(txt)
    if 'media' in t['entities']:
        img_url = t['entities']['media'][0]['media_url_https']
        txt = '<a href="{}">&#8205;</a>'.format(img_url) + txt
        #txt = txt.rsplit('https://', 1)[0]
    url = TWEET_BASE_URL + t['id_str']
    msg = MSG.format( NAME=name, TEXT=txt, URL=url)
    try: send_message(msg)
    except urllib.error.HTTPError as error:
        print('ID:\n{}\nMESSAGE: \n{}\nRESULT:\n{}\n\n\n'.format(t['id_str'], msg, error.read()))
    time.sleep(SLEEP)
    tweet_id = t['id']
if len(tweets): 
    with open(STATE_FILE, "wb") as fw: pickle.dump(tweet_id, fw)
