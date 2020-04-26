# ------------------------------------------------  #
# Python kommt ueberhaupt nicht mit umlauten klar   #
# Auch nicht in Kommentaren!                        #
# ------------------------------------------------- #  

#USER: UEBERALLBOTS
#@: @uberallbots
#PW: BotsInMyPants
#Dev-name: Piggud
import time

import tweepy


# ---------------------------------------------------------------------- #
# Hier alles an Notizen:
# um zu sehen, welcher typ etwas ist: type(Object)

# # Cursor hier mit vorsicht verwenden; kann auslaufen und spuckt einen error aus
# # Loesung:
# try:
#   yield cursor.next()
# except tweepy.RateLimitError:
#   time.sleep(15 * 60) # 15 Minuten warten

# ---------------------------------------------------------------------- #

# TODO
# answer(String templateMitFill, Tweet tweetDerBeantwortetWird)
# bsp: answer(dumbify(prepTemplate(template, theme)), inputTweet)

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
def getRandomTemplate(templates):
    pass


# gitb den nächsten zu bearbeitenden Tweet aus einer api wieder
def getNextTweet(api):
    return api.get_list
    pass

# ---------------------------------------------------------------------- #
# MainLoop:

# Bitte geheim halten:
CONSUMER_KEY = '8KksbsyJJGDquDInzOhUnLDnT'
CONSUMER_SECRET = 'Wpadb0rR8LQeFEocJuED3Uix6UGIiQltaqIeWxCy3PvjxM5xBn'
ACCESS_KEY = '1244695367284817922-oHRFPkSICOg1YF48ddlmXBPkEPHP5f'
ACCESS_SECRET = 'kik1JvgMJ3zHVb9rD1FZ89yqp62XaqnlWSWbagGVLnMUT'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
inLoop = 1

while inLoop == 1:
    nextTweet = getNextTweet(api)
    templates = getTemplatesFromFile("./templates.txt")
    theme = "die Wirtschaftskonjunktur der deutschan Nation"
    answer(dumbify(prepTemplate(getRandomTemplate(templates), theme)), nextTweet)
    time.sleep(60)
    # 1 Minute sollte reichen, um nachdenken und tweet formulieren zu simulieren. Vllt mehr random

