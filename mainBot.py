# ------------------------------------------------  #
# Python kommt ueberhaupt nicht mit umlauten klar   #
# Auch nicht in Kommentaren!                         #
# ------------------------------------------------- #  

#USER: UEBERALLBOTS
#@: @Gerhards1966S
#PW: BotsInMyPants
#Dev-name: Piggud
import tweepy

# um zu sehehn, welcher typ etwas ist: type(Object)

# Bitte geheim halten:
CONSUMER_KEY = '8KksbsyJJGDquDInzOhUnLDnT'
CONSUMER_SECRET = 'Wpadb0rR8LQeFEocJuED3Uix6UGIiQltaqIeWxCy3PvjxM5xBn'
ACCESS_KEY = '1244695367284817922-oHRFPkSICOg1YF48ddlmXBPkEPHP5f'
ACCESS_SECRET = 'kik1JvgMJ3zHVb9rD1FZ89yqp62XaqnlWSWbagGVLnMUT'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
# durch api kann man sich alles abholen
# Objekte sind wie ResultSets in Datenbanken zu behandeln, nur einfacher

FILE_NAME_ID = 'last_seen_id.txt'

inLoop = 1
tweetCursor = tweepy.Cursor(api.mentions_timeline)

while inLoop:
    try:
        # cursor.next()
        pass
    except tweepy.RateLimitError:
        # time.sleep(15*60)
        pass

# """ followed jedem follower zurueck """
# for follower in tweepy.Cursor(api.followers).items():
#    follower.follow()

# # Cursor hier mit vorsicht verwenden; kann auslaufen und spuckt einen error aus
# # Loesung:
# try: 
#   yield cursor.next()
# except tweepy.RateLimitError:
#   time.sleep(15 * 60) # 15 Minuten warten

# """ printet jeden tweet in der timeline """
# mentions = api.home_timeline()
# for tweet in mentions:
#     print(tweet.text)

# print('mentions:')
# mentions = api.mentions_timeline()
# for mention in mentions:
#     print(mention.author.name)
#     print(mention.text)

# print('\ntimeline:')
# tweets = api.home_timeline()
# for tweet in tweets:
#     print(tweet.text)
    
# TODO
# answer(String templateMitFill, Tweet tweetDerBeantwortetWird)
# bsp: answer(dumbify(prepTemplate(template, theme)), inputTweet)

# Zieht sich die zuletzt gesehene ID aus der Textdatei
def retrieve_last_seen_id(file_name):
    f_read = open(FILE_NAME_ID, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

# Speichert die zuletzt gesehene ID in der Textdatei
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(FILE_NAME_ID, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# Antowrtet auf Tweet
def answer(templateWithContent, tweetToAnswer):
    
    pass

# Füllt einen String mit Themen
def prepTemplate(templateToFill, content):
    
    pass

# Entfernt einige wenige Buchstaben/ verdreht sie
# (dient der Menschlichkeit eines Templates)
def dumbify(inputText):
    
    pass

# Gibt die gewuenschte Speicherstruktur, gefüllt mit Templates wieder
# bsp: var antworten = getTeamplatesFromFile("./antworten.txt")
def getTemplatesFromFile(filepath):

    pass


# gibt einen einzelnen. zufälligen String wieder aus dem gegebenen Speichermedium (etwa Array oder List)
def getRandomTemplate():

    pass

