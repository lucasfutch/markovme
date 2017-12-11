import abc
import markovify
import settings
import os

class MainTemplate:
    currentUserNumber =0
    def __init__(self):
        # MainTemplate.currentUserNumber keeps tracks of the number of MainTemplate objects created. We use that number to create a unique textfile for each time
        #getPredictedText is called. This will allow multiple users to use the service at the same time.
        MainTemplate.currentUserNumber = (MainTemplate.currentUserNumber +1) % 1000

    def PredictText(self,data):
        settings.init(self)   #loading global varibales saved in settings.py
        self.collectText(data)  #collecting data from user
        self.createTextPath(MainTemplate.currentUserNumber)  #create Textfile with the currentUserNumber
        self. parseText(data,MainTemplate.currentUserNumber)  #cleans the data from the user and  saves it in a textfile with the currentUserNumber
        return self.getPredictedText(MainTemplate.currentUserNumber) # gets the Predicted text from the given textfile

    def collectText(self, data):
        self.data=data

    def createTextPath(self, userNumber):
        filePath = open("static/trainingText"+str(userNumber)+".txt", 'w')


    def getPredictedText(self,userNumber):
        print(userNumber)
        with open("static/trainingText"+str(userNumber)+".txt") as f:
            text = f.read()
        text_model = markovify.Text(text)
        predicted_text = text_model.make_sentence()   #using markovify to get the predicted text.
        os.remove("static/trainingText"+str(userNumber)+".txt") #removing the text file after using it. We no longer need it as we have already obtained the predicted text
        #markovify returns none if it cannot predict a sentence. It is due to lack of enough data.
        if predicted_text==None:
            return "Not sufficient data. More Needed to predict."
        return predicted_text