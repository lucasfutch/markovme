import os

from MainTemplate import MainTemplate
import sys
from pathlib import Path

class TextFile(MainTemplate):
    def parseText(self, data):
        my_file = Path("static/trainingText.txt")
        if my_file.is_file():
            try:
                os.remove("static/trainingText.txt")
            except OSError:
                pass
        with open('static/trainingText.txt', 'a') as TextFile:
            TextFile.write(data)

        TextFile.close()
