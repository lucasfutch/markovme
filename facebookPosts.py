import os

from MainTemplate import MainTemplate
import sys
from pathlib import Path



class facebookPosts(MainTemplate):

    # writing the data to a textfile with the currentUserNumber.
    def parseText(self,data,userNumber):
        data = data['x']
        with open("static/trainingText"+str(userNumber)+".txt", 'a') as fbPostFile:
            for post in data:
                f_path = post + "\n"
                fbPostFile.write(post)

        fbPostFile.close()
