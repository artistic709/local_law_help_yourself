import time
import telepot

database=[]

def subscribe(uid,courseid):
	exist=0
	for i in database:
		if i[0]==uid and i[1]==courseid:
			exist=1
	if exist==0:
		database.append((uid,courseid))
		bot.sendMessage(uid, " Subscribed ")
		print(database)

def alarm(uid,courseid):
	for i in database:
		if i[1]==courseid:
			bot.sendMessage(i[0], " Rollcall !!! ")

def homework(uid,courseid,nextweek):
	if nextweek=='1':
		for i in database:
			if i[1]==courseid:
				bot.sendMessage(i[0], " There's new homework for nextweek. ")
	else:
		for i in database:
			if i[1]==courseid:
				bot.sendMessage(i[0], " There's new homework in previous week. ")

def unsubscribe(uid,courseid):
	pass

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
    	text=msg['text'].split(" ")
    	if text[0]=='subscribe':
    		subscribe(chat_id,text[1])
    	if text[0]=='alarm':
    		alarm(chat_id,text[1])
    	if text[0]=='homework':
    		homework(chat_id,text[1],text[2])
    	#if text[0]==unsubscribe:


TOKEN = "295434152:AAEK5cEciqoCh24NB-U8cQGiqh-s8wHnnio" #insert BOT TOKEN

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

while 1:
    time.sleep(10)
