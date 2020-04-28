# ------------------------------------------------  #
# Python kommt ueberhaupt nicht mit umlauten klar   #
# Auch nicht in Kommentaren!                        #
# ------------------------------------------------- #  

#USER: UEBERALLBOTS
#@: @Gerhards1966S
#PW: BotsInMyPants
#Dev-name: Piggud
import random
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

# Swap function
def swap(list, pos1, pos2):
    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)
    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)
    return list

# Antowrtet auf Tweet
def answer(templateWithContent, tweetToAnswer):
    pass


# Füllt einen String mit Themen
def prepTemplate(templateToFill, content):
    return templateToFill.replace(";;;;", content)


# Entfernt einige wenige Buchstaben/ verdreht sie
# (dient der Menschlichkeit eines Templates)
def dumbify(inputText, gradeOfDestruction):
    listOfChars = list()
    for x in inputText:
        listOfChars.append(x)

    for y in range(round(gradeOfDestruction/2)):
        listOfChars.remove(random.choice(listOfChars))

    for z in range(round(gradeOfDestruction/2)):
        ranNum = random.randint(0, len(listOfChars)-1)
        swap(listOfChars, ranNum, ranNum+1) # len(list)

    return "".join(listOfChars)


# Gibt die gewuenschte Speicherstruktur, gefüllt mit Templates wieder
# bsp: var antworten = getTeamplatesFromFile("./antworten.txt")
def getTemplatesFromFile(filepath):
    try:
        file = open(filepath, "r")
        contents = file.readlines()
    finally:
        file.close()
    print("loaded templates!")
    return contents

# gibt einen einzelnen. zufälligen String wieder aus dem gegebenen Speichermedium (etwa Array oder List)
def getRandomTemplate(templates):
    return random.choice(templates)

# Sucht mit dem #Corona nach den aktuellsten deutschen Tweets
def searchForTweets(api, hashtag):
    return api.search(hashtag)

def reply_to_tweets(hashtag):
    search = searchForTweets(api, hashtag)
    nextTweet = search[0]
    last_seen_id = retrieve_last_seen_id(FILE_NAME_ID)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')

    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME_ID)
        api.update_status("@" + mention.user.screen_name + "Antwort", mention.id)

#   templates = getTemplatesFromFile("./templates.txt")
    theme = "die Wirtschaftskonjunktur der deutschan Nation"
#   answer(dumbify(prepTemplate(getRandomTemplate(templates), theme)), nextTweet)
    api.update_status("@" + nextTweet.user.screen_name + " I like this.", nextTweet.id)
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
FILE_NAME_ID = 'last_seen_id.txt'
FILE_NAME_TEMPLATES = 'templates.txt'

while True:
    reply_to_tweets("#Corona")
    time.sleep(60)
    # 1 Minute sollte reichen, um nachdenken und tweet formulieren zu simulieren. Vllt mehr random

