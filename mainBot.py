# ------------------------------------------------  #
# Python kommt ueberhaupt nicht mit umlauten klar   #
# Auch nicht in Kommentaren!                        #
# ------------------------------------------------- #  

# USER: UEBERALLBOTS
# @: @Gerhards1966S
# PW: BotsInMyPants
# Dev-name: Piggud
import random
import time
import tweepy

# Bitte geheim halten:
CONSUMER_KEY = '8KksbsyJJGDquDInzOhUnLDnT'
CONSUMER_SECRET = 'Wpadb0rR8LQeFEocJuED3Uix6UGIiQltaqIeWxCy3PvjxM5xBn'
ACCESS_KEY = '1244695367284817922-oHRFPkSICOg1YF48ddlmXBPkEPHP5f'
ACCESS_SECRET = 'kik1JvgMJ3zHVb9rD1FZ89yqp62XaqnlWSWbagGVLnMUT'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
FILE_NAME_ID = 'lastSeenId.txt'
FILE_NAME_ID_MENTIONS = 'lastSeenIdMentions.txt'
FILE_NAME_TEMPLATES = 'templatesToFill.txt'
FILE_NAME_TEMPLATES_NO_HASH = 'templatesDone.txt'


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

# gibt zufällige Zahl mit 10% Abweichung um x aus
def genBufferTime(x):
    x_up = x * 1.10
    x_down = x * 0.9
    return random.randint(x_down, x_up)


# Zieht sich die zuletzt gesehene ID aus der Textdatei
def retrieve_lastSeenId(fileName):
    fRead = open(fileName, 'r')
    lastSeenId = int(fRead.read().strip())
    fRead.close()
    return lastSeenId


# Speichert die zuletzt gesehene ID in der Textdatei
def storeLastSeenId(lastSeenId, fileName):
    fWrite = open(fileName, 'w')
    fWrite.write(f"{str(lastSeenId)}")
    fWrite.close()
    return


# Swap function für Elemente einer Liste
def swap(list, pos1, pos2):
    firstEle = list.pop(pos1)
    secondEle = list.pop(pos2 - 1)
    list.insert(pos1, secondEle)
    list.insert(pos2, firstEle)
    return list


# Beantwortet alle Tweets, die
# 1. an diesen Bot gerichtet sind
# 2. noch keine Antwort haben
def answerToTweets():
    lastSeen = retrieve_lastSeenId(FILE_NAME_ID_MENTIONS)
    print(lastSeen)
    if lastSeen < 1:
        mentions = api.mentions_timeline()
        pass
    else:
        mentions = api.mentions_timeline(lastSeen)
        pass
    templatesWithHashtag = getTemplatesFromFile(FILE_NAME_TEMPLATES)
    templatesWithoutHashtag = getTemplatesFromFile(FILE_NAME_TEMPLATES_NO_HASH)
    for mention in mentions:
        if mention.id != lastSeen:
            if mention.text.find("bot") != -1:
                answer("Was redest du da?", mention)
                pass
            else:
                if mention.text.find("#") != -1:
                    theme = mention.entities['hashtags'][0].get("text")
                    answer(dumbify(prepTemplate(getRandomTemplate(templatesWithHashtag), theme), 2), mention)
                else:
                    answer(dumbify(getRandomTemplate(templatesWithoutHashtag), 2), mention)
                pass
            pass
        else:
            print("no new Entries!")
        storeLastSeenId(mention.id, FILE_NAME_ID_MENTIONS)
        time.sleep(genBufferTime(90))
        pass


# Antwortet auf Tweet
def answer(templateWithContent, tweetToAnswer):
    api.update_status(f"@{tweetToAnswer.user.screen_name} {templateWithContent}", tweetToAnswer.id)


# Füllt einen String mit Themen
def prepTemplate(templateToFill, content):
    return templateToFill.replace(";;;;", content)


# Entfernt einige wenige Buchstaben/ verdreht sie
# (dient der Menschlichkeit eines Templates)
def dumbify(inputText, gradeOfDestruction):
    listOfChars = list()
    for x in inputText:
        listOfChars.append(x)

    for y in range(round(gradeOfDestruction / 2)):
        listOfChars.remove(random.choice(listOfChars))

    for z in range(round(gradeOfDestruction / 2)):
        ranNum = random.randint(0, len(listOfChars) - 1)
        swap(listOfChars, ranNum, ranNum + 1)  # len(list)

    return "".join(listOfChars)


# Gibt die gewuenschte Speicherstruktur, gefüllt mit Templates wieder
# bsp: var antworten = getTeamplatesFromFile("./antworten.txt")
def getTemplatesFromFile(filepath):
    try:
        file = open(filepath, "r")
        contents = file.readlines()
    finally:
        file.close()
    return contents


# gibt einen einzelnen, zufälligen String wieder aus dem gegebenen Speichermedium (etwa Array oder List)
def getRandomTemplate(templates):
    return random.choice(templates)


# Sucht mit dem hashtag nach den aktuellsten deutschen Tweets
def searchForTweets(api, hashtag):
    return api.search(hashtag, "de")


# Antwortet auf den aktuellsten Tweet aus dem mitgegebenen Hashtag
def replyToSearchedTweets(hashtag):
    search = searchForTweets(api, hashtag)
    nextTweet = search[0]
    api.update_status("@" + nextTweet.user.screen_name + " I like this.", nextTweet.id)
    pass


# Gibt die Top-Hashtags aus der Region aus
def printTrends(place):
    trends_result = api.trends_place(place)
    for trend in trends_result[0]["trends"]:
        print(trend["name"])


# ---------------------------------------------------------------------- #
# MainLoop:

while True:
    answerToTweets()
    # replyToTweets("#Corona")
    # printTrends(23424829)
    time.sleep(genBufferTime(120))
