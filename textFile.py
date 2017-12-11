import os

from MainTemplate import MainTemplate
import sys
from pathlib import Path

class TextFile(MainTemplate):

    #writing the data to a textfile with the currentUserNumber.
    def parseText(self, data,userNumber):
        with open("static/trainingText"+str(userNumber)+".txt", 'a') as TextFile:
            TextFile.write(data)
        TextFile.close()
