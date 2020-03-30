#USER: UEBERALLBOTS
#@: @uberallbots
#PW: BotsInMyPants
#Dev-name: Piggud
#Access_Token: 1244695367284817922-oHRFPkSICOg1YF48ddlmXBPkEPHP5f
#Access_Secret: kik1JvgMJ3zHVb9rD1FZ89yqp62XaqnlWSWbagGVLnMUT
import tweepy

CONSUMER_KEY = '8KksbsyJJGDquDInzOhUnLDnT'
CONSUMER_SECRET = 'Wpadb0rR8LQeFEocJuED3Uix6UGIiQltaqIeWxCy3PvjxM5xBn'
ACCESS_KEY = '1244695367284817922-oHRFPkSICOg1YF48ddlmXBPkEPHP5f'
ACCESS_SECRET = 'kik1JvgMJ3zHVb9rD1FZ89yqp62XaqnlWSWbagGVLnMUT'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print('My Bot')