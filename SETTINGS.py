# Twitter AUTH:
APP_KEY = 'APP_KEY_HERE' 
APP_SECRET = 'APP_SECRET_HERE' 
OAUTH_TOKEN = 'TOKEN_HERE'
OAUTH_TOKEN_SECRET = 'TOKEN_SECRET_HERE'

# Telegram options:
TELEGRAM_CHANNEL = 'CHANNEL_NAME_HERE'
TELEGRAM_TOKEN = 'TOKEN_HERE'

# Misc:
TWITTER_USER_NAME = 'USER_NAME_HERE'
MSG = '<b>{NAME}</b>:\n{TEXT}\n\n<a href="{URL}">Source</a>'

# Technical stuff:
TWEET_BASE_URL = 'https://twitter.com/i/web/status/'
STATE_FILE = 'state.p'
SLEEP = 3
TG_LINK = 'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=@{CHANNEL}&text={MESSAGE}&parse_mode=html'
UNSUPPORTED_TAGS = ['<span class="twython-tweet-suffix">', '<span class="twython-tweet-prefix">', '</span>', 'class="twython-url"', 'class="twython-media"', 'class="twython-mention"', 'class="twython-hashtag"', 'class="twython-symbol"', ]
