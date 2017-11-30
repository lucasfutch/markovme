import os

from MainTemplate import MainTemplate
import sys
from pathlib import Path

class TextFile(MainTemplate):
    def parseText(self, data):
        os.rename("static"+data, "static/trainingText.txt")