import os

from MainTemplate import MainTemplate
import sys
from pathlib import Path
import tweepy
import settings




class twitter(MainTemplate):

    #collecting data from twitter. We use tweepy for that.
    def collectText(self, data):
        settings.init(self)  #loading the global variables
        # twitter authentication stuff
        auth = tweepy.OAuthHandler("t1lQX1VkiCf3dHC4z9XOtf8wy", "rh2KjvPIakeymfrMzQYXtR5T3AFYB3Rt1yq4ZW2YcL5Eji2EpI")
        auth.set_access_token("72186647-4qqJpl6DpSKEqVhDsLxQjmqTcq8YyoRwl1ow2xaZG",
                              "q9SsVA3v8BJSFqZKrEAErbJMmfM3VzNRCLiWf0DVJTNkm")
        twitter_api = tweepy.API(auth)

        # twitter user data.
        # can change the amount of tweets/items requested or each one
        # check that the textbox was not empty
        try:
            if data['user1']!="":
                #removing @ if given
                if data['user1'][0]=='@':
                    data['user1']=data['user1'][1:]

                #getting twitter data
                getUser1Tweets = tweepy.Cursor(twitter_api.user_timeline, q="* -filter:retweets -filter:replies", screen_name=data['user1'], include_rts = False).items(200)
                # this gets every tweet and you can manipulate them
                for result in getUser1Tweets:
                    #saving the tweets in a global variable called retrieve_data
                    settings.retrieve_data.append(result.text);
                    #print(type(result.text))
        except Exception as e:
            #if no tweets were collected of the user1
            if len(settings.retrieve_data)<2:
                settings.errorlog = "We were not able to collect tweets of " +data['user1']
        try:
            if data['user2'] != "":
                if data['user2'][0]=='@':
                    data['user2']=data['user2'][1:]
                getUser2Tweets = tweepy.Cursor(twitter_api.user_timeline, q="* -filter:retweets -filter:replies", screen_name=data['user2'], include_rts = False).items(200)
                for result in getUser2Tweets:
                    settings.retrieve_data.append(result.text);
        except Exception as e:
            if len(settings.retrieve_data) < 4:
                if settings.errorlog=='':
                    settings.errorlog = "We were not able to collect tweets of " +data['user2']+". Please make sure that the twitter handle is correct."
                else:
                    settings.errorlog=settings.errorlog + ' and '+data['user2']+'. Please make sure that the twitter handles are correct.'


    def parseText(self, data,userNumber):
        #if there were no error than save the tweets in the textfile
        if settings.errorlog=='':
            with open("static/trainingText"+str(userNumber)+".txt", 'a') as twitterFile:
                for tweet in settings.retrieve_data:
                    f_path = tweet+ "\n"
                    twitterFile.write(tweet)

            twitterFile.close()


    def getPredictedText(self,userNumber):
        #if errors return them else call the getPredicted from the MainTemplate
        if settings.errorlog!='':
            return settings.errorlog
        else:
            return MainTemplate.getPredictedText(self,userNumber)
