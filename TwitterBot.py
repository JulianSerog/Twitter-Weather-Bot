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

#create an infinite loop that updates the status to whatever the weather is currently
while True:
	#set a string here based on weather
	print pywapi.get_location_ids("Athens")
	weather_com_result = pywapi.get_weather_from_weather_com('USGA0027')
	message = "It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Athens, Georgia.\n"
	api.update_status(message)
	time.sleep(3600) #sleep for 1 hour