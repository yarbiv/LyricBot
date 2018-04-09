from twython import Twython
import sys

APP_KEY = 'INSERT TWITTER APP KEY HERE'
APP_SECRET = 'INSERT TWITTER APP SECRET KEY HERE'

OAUTH_TOKEN = 'INSERT TWITTER OAUTH TOKEN HERE'
OAUTH_TOKEN_SECRET = 'INSERT TWITTER SECRET TOKEN HERE'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


with open("tweet.txt") as f:
    tweet = f.read()

twitter.update_status(status= sys.argv[1] + "\n" + tweet[3:])