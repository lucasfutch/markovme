import abc
import markovify

class MainTemplate:

    def __init__(self):
        self.text=""

    def PredictText(self,text):
        self.collectText(text)
        self. parseText(text)
        return self.getPredictedText()

    def collectText(self, text):
        self.text = text

    def getPredictedText(self):
        with open("static/trainingText.txt") as f:
            text = f.read()
        text_model = markovify.Text(text)
        predicted_text = text_model.make_sentence()
        return predicted_text