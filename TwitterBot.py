#!/usr/bin/python

#import frameworks
import tweepy, time, sys, pywapi, string

CONSUMER_KEY = 'zOqCHqDWjhcqnxl2DWd4QBtsX'
CONSUMER_SECRET = 'hjXtgqS40u9paLEw99Wlp1PKrbOeGAF27KGQ4Yx2gEfg40Q4uk'
ACCESS_KEY = '701621684198047744-xXwmYg4z55nsMImCmd6G1yao1YoaA59'
ACCESS_SECRET = 'ILJpeb7VFnm98HBdZCHglysHkRvCW3bS2QL5MR3kX6iLs'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

"""
#USED FOR TESTING WITH READING IN FILES
#grab file from command line arguements
argfile = str(sys.argv[1])


#create a file reader
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

#test for reading in file
for line in f:
    api.update_status(status=line)
    time.sleep(15)#Tweet each line in file every 15 seconds
"""

previousTweet = ""
#create an infinite loop that updates the status to whatever the weather is currently
while True:
	#print pywapi.get_location_ids("Athens") #gets all location ID's for 'athens', prints to console, I used this to find the code for Athens, Georgia
	yahoo_result = pywapi.get_weather_from_yahoo('USGA0027') #Athens Georgia code
	#update new tweet text
	message = str(yahoo_result['condition']['text']).lower() + " and " + str(yahoo_result['condition']['temp']) + "C now in Athens, Georgia.\n"
	#to grab first status in tweepy.Cursor
	counter = 0 
	#find a more efficient way of doing this, tweepy documentation is tricky but this should solve the issue for now
	for status in tweepy.Cursor(api.user_timeline).items():
		if counter == 0:
			previousTweet = status.text
			print "previous: " + previousTweet
			break
		counter += 1
	#print statements for error checking
	print "current: " + message.strip(" ")
	#only tweet when weather has changed
	print "old tweet == new tweet: "
	print message.strip(" ") == previousTweet.strip(" ")
	if str(message) != str(previousTweet):
		try:
			api.update_status(message)
			print "new tweet posted"
		except:
			print "tweet matched an old tweet, waiting 30 minutes to attempt to update..."
			pass

	time.sleep(1800) #sleep for 30