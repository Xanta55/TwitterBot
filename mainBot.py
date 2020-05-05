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
FILE_NAME_TEMPLATES_CORONA = 'templatesCorona.txt'


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
    noRepliesYet = 1
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
            noRepliesYet = 0
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
        storeLastSeenId(mention.id, FILE_NAME_ID_MENTIONS)
        time.sleep(genBufferTime(90))
        pass
    if noRepliesYet == 1:
        print("no new Replies!")
        chooseActivity(noRepliesYet)
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


# Sucht die aktuellsten deutschen Tweets zu einem gewünschten Hashtag
def searchForTweets(api, hashtag, lastId):
    return api.search(q = hashtag, lang = "de", since_id = lastId)


# Sucht nach den aktuellsten Tweets mit dem übergebenen Hashtag
# Checkt, ob auf diesen Tweet nicht bereits geantwortet wurde
# Fügt ein Hashtag für die Antwort an, falls nicht vorhanden
def replyToSearchedTweets(hashtag):
    search = searchForTweets(api, hashtag, retrieve_lastSeenId(FILE_NAME_ID))
    nextTweet = search[0]
    templatesWithHashtag = getTemplatesFromFile(FILE_NAME_TEMPLATES)
    storeLastSeenId(nextTweet.id, FILE_NAME_ID)
    answer(dumbify(prepTemplate(getRandomTemplate(templatesWithHashtag), hashtag), 1), nextTweet)
    pass

def tweetCoronaPost():
    api.update_status(getRandomTemplate(getTemplatesFromFile(FILE_NAME_TEMPLATES_CORONA)))
    pass


# Gibt die Top-Hashtags aus der Region aus
# WOEID Code für Deutschland 23424829
def chooseTrend(place):
    trends_result = api.trends_place(place)
    data = trends_result[0] 
    trends = data['trends']
    names = [trend['name'] for trend in trends]
    return names[random.randint(0, 2)]

# Wählt zufällig aus, ob auf Mentions geantwortet, nach #Corona gesucht oder nach einen
# der Top 3 Trends gesucht wird
def chooseActivity(min):
    print("Choosing activity...")
    rand = random.randint(min, 4)
    if rand == 0:
        print("Answering Mentions...")
        answerToTweets()
    elif rand == 1:
        print("Searching for Tweets with the Hashtag #Corona...")
        replyToSearchedTweets("#Corona")
    elif rand == 2:
        print("Searching for trending Tweets...")
        replyToSearchedTweets(chooseTrend(23424829))
    elif rand == 3:
        print("Tweeting about Corona...")
        tweetCoronaPost()
    pass
    

# ---------------------------------------------------------------------- #
# MainLoop:
# Wartet nach jeder Aktivität 27-33 Minuten

while True:
    chooseActivity(0)
    print("Done, waiting for next round...")
    time.sleep(genBufferTime(30) * 60)
