import os

from MainTemplate import MainTemplate
import sys
from pathlib import Path



class facebookPosts(MainTemplate):

    def parseText(self,data):
        my_file = Path("static/trainingText.txt")
        if my_file.is_file():
            try:
                os.remove("static/trainingText.txt")
            except OSError:
                pass
        data = data['x']
        with open('static/trainingText.txt', 'a') as fbPostFile:
            for post in data:
                f_path = post + "\n"
                fbPostFile.write(post)

        fbPostFile.close()
