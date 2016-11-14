# -*- coding: utf-8 -*-
import random
import sys
import time
import telepot

TOKEN = "261445963:AAEepSBgL9y0ni7Q0OtsZEIhSI1wAzv1lKg"
bot = telepot.Bot(TOKEN)
log = open('indignityBot\\log.txt','a+')
startUpTime = int(time.time())-3660

helpText = '''This bot will help you to _communicate_ people in a more effective way

/start : Start Up the bot
/help : Print help text
/emote : Some emotes (Use private chat to learn how to use)
/double : Insult as You + adj + noun
/triple : Insult as You + adj + adj + noun
/fuckoff : Insult as Verb + noun + noun
/suggestion : A friendly suggestion
/bullshit : Allergic to bullshit?
'''

ar1=["bastard","battle-axe","blowhard","chromedome","cow","cow pie","coward","dingle berry","dog","elephant","four eyes","fucker","nancy boy","hag","hemorrhoid","jackass","maggot","pervert","moron","runt","nerd","panzy","pig","pipsqueak","prick","putz","reject","retard","shmuck","skank","skeezer","slob","sloth","slut","snaggletooth","son of a bitch","stick","mother fucker","toad","toothpick","tramp","weakling","weirdo","homo","faggit","queerbait","queer","fag","flamer","fudgepacker","butt pirate","dyke","shitspitter","queefer","shitstain","jerkoff","jackoff","pimple","zit","midget","sicko","bitch"]
ar2=["butt","corn","cum","horse","scum","slime","douche","jizz","piss"]
ar3=["bag","ball","brain","bucket","face","head","hole","nugget","wad","breath"]
ar5=["goat","monkey's balls","ballsack","horse's gonads"]
ar6=["piece","sack"]
ar7=["ass","asscrack","ballsack","butt","butthole","clit","cock","cunt","dick","nipple","penis","pussy","shit","titty","vagina","twat","schlong","snatch","scrotum","nutsack","pile of shit","camel toe","cooch","carpet"]
ar8=["cheese","crap","dip"]
ar9=["bitch","booger","cunt","dork","ho","pecker","pussy","tit","whore"]
ar10=["wart"]
ar11=["nut","turd","cock"]
ar12=["ballsack"]
ar13=["annoying","anorexic","atrocious","scummy","awkward","brainless","dirty","freakish","funky","girating","hairy","idiotic","insane","lowlife","moronic","old","paranoid","putrid","retarted","sick","silly","skinny","smelly","twisted","ugly","weird","gay","pathetic","wretched","little","scrawny","lowlife","disgusting","nasty"]
ar14=["skeez","sleaze"]
ar15=["fuck"]
ar16=["stupid","dumb","lazy","fat"]
ar17=["suck","fuck","lick","eat","surf","munch"]
ar18=["shit","crap","dung","filth","nothing"]
ar19=["listen to","put up with","deal with"]
ar20=["shit","guff","garbage","bullshit","fucking shit","damn bullshit"]
ar21=["one more time","any more"]
ar22=["deck you in the fucking face","punch your fucking lights out","knock your block off","smack you all over the walls","bitch slap your fucking ass","kick you in the ballsack","open up a can of whoopass","punch your ass into last week","smash your fucking face in"]
ar23=["monkey","horse","cow","pig","goat"]
ar24=["shoot yourself","fuckoff","fuck a pig in the ass","take a long walk off a short pier","to hell","jerk yourself","fuck yourself","shove a cucumber up your asshole"]
ar25=["mother fucker","cock sucker","bitch mother fucker","dickhead","son of a bitch mother fucker","son of a bitch","piece of fucking shit","sack of shit","cunt bitch"]
ar26=["cock sucking","dick licking","butthole surfing","asscrack licking","fucking","fuckass","scum eating","piss drinking","cum guzzling"]
ar27=["needle","stumpy","manuer"]

emotes = {'finger' : u'''…………………./´¯/)
………………..,/¯../
………………./…./
…………./´¯/’…’/´¯¯`·¸
………./’/…/…./……./¨¯\\
……..(‘(…´…´…. ¯~/’…’)
………\……………..’…../
……….”…\………. _.·´
…………\…………..(
…………..\………….\…''',
                    'hungry' :u'''ಠﭛಠ''',
                    'old' :u'''ತಎತ''',
                    'sad' :u'''ಥ_ಥ''',
                    'soulless' : u'''ರ_ರ''',
                    'heya' : u'''(☞ﾟヮﾟ)☞''',
                    'heyaback' : u'''☜(ﾟヮﾟ☜)''',
                    'finger2':u'''╭∩╮(Ο_Ο)╭∩╮''',
                    'shrug' : u'''¯\_(ツ)_/¯ ''',
                    'table' : u'''(╯°□°）╯︵ ┻━┻''',
                    'disapproval' : u'''ಠ_ಠ''',
                    'sir' : u'''ಠ_ರೃ''',
                    'flip' : u'''t(-.-t)''',
                    'smug' :u'''(‾ ⌣ ‾)''',
                    'hug' : u'''(っ◕‿◕)っ''',
                    'lenny' : u'''( ° ͜ ʖ °)﻿''',
                    'love' : u'''( ˘ ³˘)♥''',
                    'evil' : u'''ಠ◡ಠ''',
                    'zoidberg' :u'''(\/)(°,,,°)(\/)''',
                    'but' : u'''(°ロ°):point_up:''',
                    'table' : u'''(╯°□°）╯︵ ┻━┻''',
                    'angrytable' : u'''(ノಠ益ಠ)ノ彡┻━┻''',
                    'backtable' : u'''┬─┬ノ( º _ ºノ)''',
                    'mother' : u''' O
/_\ ___O Yeah your mom is fun
/ / JJ \\ ''',
                    'orly' : u'''{o,o}
/)__) 
_"_"_ 
O RLY?'''}

def emoteHelp():
    ret = "This command works like /emote <emote> where <emote> is replaced by one of the following\n\n"
    for key in emotes.keys():
        ret+= key + ' : ' + emotes[key] +'\n'
    return ret

def logMessage(msg):
    chatType = msg['chat']['type']
    sender = str(msg['from']['id']) +' ('+msg['from']['first_name']
    if 'last_name' in msg['from']:
        sender = sender + ' '+ msg['from']['last_name'] + ") "
    else:
        sender = sender + ') '
    timestamp = str(msg['date'])
    msgText= msg['text']

    if chatType == 'private':
        strToFile = (timestamp + ': ' + sender + 'TO '+ str(msg['chat']['id'])+' (private chat) ' +'"'+ msgText+'"\n').encode('utf-8','replace')
        log.write(strToFile)
    if chatType == 'group' or chatType == 'supergroup':
        strToFile = (timestamp + ': ' + sender + 'TO '+ str(msg['chat']['id'])+' ('+msg['chat']['title']+') ' +'"'+ msgText+'"\n').encode('utf-8','replace')
        log.write(strToFile)
    log.flush()

def addUser(msgFrom, msgDate):
    userRName = msgFrom['first_name']
    userID = str(msgFrom['id'])
    if 'last_name' in msgFrom:
        userRName = userRName + ' ' +msgFrom['last_name']
    if(checkFile(userID,'indignityBot\\users.txt')):
        users = open('indignityBot\\users.txt','a+')
        strToFile = (userID +', ' + userRName +', '+str(msgDate)+'\n').encode('utf-8','replace')
        users.write(strToFile)
        users.close()

def checkFile(search, fileName):
    file = open(fileName,'r+')
    for line in file:
        if search in line:
            file.close()
            return False
    file.close()
    return True

def single():
     word2 = ar2[random.randrange(0,len(ar2))]
     word2 += ar3[random.randrange(0,len(ar3))]
     return word2

def doubleCombo():
    word1 = ar13[random.randrange(0,len(ar13))]
    word2 = random.randint(0,1)
    if word2:
        word2 = ar1[random.randrange(0,len(ar1))]
    else:
        word2 = ar2[random.randrange(0,len(ar2))]
        word2 += ar3[random.randrange(0,len(ar3))]

    return 'You ' + word1 + ' ' + word2

def tripleCombo():
    word1 = ar2[random.randrange(0,len(ar2))]
    word2 = ar17[random.randrange(0,len(ar17))]
    word3 = ar17[random.randrange(0,len(ar17))]
    word4 = ar7[random.randrange(0,len(ar7))]
    word5 = ar6[random.randrange(0,len(ar6))]
    word6 = ar18[random.randrange(0,len(ar18))]
    word7 = ar1[random.randrange(0,len(ar1))]
    return "You " + word1 + " " + word2 + "ing, " + word4 + " " + word3 + "ing " + word5 + " of " + word6 + " " + word7

def imperative():
    word1 = ar17[random.randrange(0,len(ar17))]
    word2 = ar23[random.randrange(0,len(ar23))]
    word3 = ar7[random.randrange(0,len(ar7))]
    word4 = ar7[random.randrange(0,len(ar7))]
    word5 = ar3[random.randrange(0,len(ar3))]
    return word1.title() + ' a ' + word2 +"'s " + word3+", "+word4+word5

def whyDontYou():
    word1 = ar24[random.randrange(0,len(ar24))]
    word2 = ar26[random.randrange(0,len(ar26))]
    word3 = ar25[random.randrange(0,len(ar25))]
    return "Why don't you go " + word1 + " you " + word2 + " " + word3

def ifIHaveTo():
    word1 = ar19[random.randrange(0,len(ar19))]
    word2 = ar20[random.randrange(0,len(ar20))]
    word3 = ar21[random.randrange(0,len(ar21))]
    word4 = ar22[random.randrange(0,len(ar22))]
    word5 = ar13[random.randrange(0,len(ar13))]
    word6 = ar7[random.randrange(0,len(ar7))]
    word7 = ar17[random.randrange(0,len(ar17))]
    return "If i have to " + word1 + " your " + word2 + " " + word3 + ", I'm gonna " + word4 + " you " + word5 + " " + word6 + " " + word7 + "er!"

def handle(msg):
    #TODO : ADD SHAKESPEAREAN INSULTS
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text' and msg['date']>startUpTime:
        msgList = msg['text'].split('@')
        msgText = msgList[0]
        intendedBot = ''
        if len(msgList)>1:
            intendedBot = msgList[1]
        if intendedBot == '' or intendedBot == 'indignitybot':
            if '/start' == msgText:
                bot.sendMessage(chat_id,'IndignityBot is at your service, you ' + single())
            if 'help' in msgText:
                bot.sendMessage(chat_id,helpText,parse_mode='Markdown')
            if '/bullshit' == msgText:
                bot.sendMessage(chat_id,ifIHaveTo())
            if '/fuckoff' == msgText:
                bot.sendMessage(chat_id,imperative())
            if '/suggestion' == msgText:
                bot.sendMessage(chat_id,whyDontYou())
            if '/triple' == msgText:
                bot.sendMessage(chat_id,tripleCombo())
            if '/double' == msgText:
                bot.sendMessage(chat_id,doubleCombo())
            if '/emote' == msgText:
                if chat_type == 'private':
                    bot.sendMessage(chat_id,emoteHelp())
                else:
                    bot.sendMessage(chat_id,"To check available emotes please use private chat\n You can start one by messaging @indignitybot")
            elif '/emote' in msgText:
                cmd =''
                emote =''
                msgText = msgText.split()
                cmd = msgText[0]
                if len(msgText)>1:
                    emote=msgText[1]

                if not emote == '':
                    if emote in emotes.keys():
                        bot.sendMessage(chat_id,emotes[emote])
                    else:
                        bot.sendMessage(chat_id,emotes['disapproval'] + '\nInvalid emote!',reply_to_message_id=msg['message_id'])
                    

        addUser(msg['from'],msg['date'])
        logMessage(msg)

bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)