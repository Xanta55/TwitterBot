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
api = tweepy.API(auth)
FILE_NAME_ID = 'lastSeenId.txt'
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

# TODO
# answer(String templateMitFill, Tweet tweetDerBeantwortetWird)
# bsp: answer(dumbify(prepTemplate(template, theme)), inputTweet)

# Zieht sich die zuletzt gesehene ID aus der Textdatei
def retrieve_lastSeenId(fileName):
    fRead = open(fileName, 'r')
    lastSeenId = int(float(fRead.read().strip()))
    fRead.close()
    return lastSeenId


# Speichert die zuletzt gesehene ID in der Textdatei
def storeLastSeenId(lastSeenId, fileName):
    fWrite = open(fileName, 'w')
    fWrite.write(f"{str(lastSeenId)}")
    fWrite.close()
    return


# Swap function
def swap(list, pos1, pos2):
    # popping both the elements from list
    firstEle = list.pop(pos1)
    secondEle = list.pop(pos2 - 1)
    # inserting in each others positions
    list.insert(pos1, secondEle)
    list.insert(pos2, firstEle)
    return list


def answerToTweets():
    lastSeen = retrieve_lastSeenId(FILE_NAME_ID)
    mentions = api.mentions_timeline(lastSeen)
    templatesWithHashtag = getTemplatesFromFile(FILE_NAME_TEMPLATES)
    templatesWithoutHashtag = getTemplatesFromFile(FILE_NAME_TEMPLATES_NO_HASH)
    for mention in mentions:
        if mention.id != lastSeen:
            if mention.text.find("bot") != -1:
                answer("Was redest du da?", mention)
            else:
                if mention.text.find("#") != -1:
                    theme = mention.entities['hashtags'][0].get("text")
                    answer(dumbify(prepTemplate(getRandomTemplate(templatesWithHashtag), theme), 1), mention)
                else:
                    answer(dumbify(getRandomTemplate(templatesWithoutHashtag), 1), mention)
                pass
            pass
        storeLastSeenId(mention.id, FILE_NAME_ID)
        time.sleep(10)
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


# gibt einen einzelnen. zufälligen String wieder aus dem gegebenen Speichermedium (etwa Array oder List)
def getRandomTemplate(templates):
    return random.choice(templates)


# Sucht mit dem #Corona nach den aktuellsten deutschen Tweets
def searchForTweets(api, hashtag):
    return api.search(hashtag, "de")


def replyToSearchedTweets(hashtag):
    search = searchForTweets(api, hashtag)
    nextTweet = search[0]
    #   templates = getTemplatesFromFile("./templates.txt")
    theme = "die Wirtschaftskonjunktur der deutschan Nation"
    #   answer(dumbify(prepTemplate(getRandomTemplate(templates), theme)), nextTweet)
    api.update_status("@" + nextTweet.user.screen_name + " I like this.", nextTweet.id)
    pass


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

