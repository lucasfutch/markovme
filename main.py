from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
import markovify
import tweepy
import settings
from flask import Flask

from MainTemplate import MainTemplate
from facebookPosts import facebookPosts
from textFile import TextFile
from twitter import twitter


#UPLOAD_FOLDER = '/uploads'
#ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
settings.init('self')

##removed the option of uploading a text file and added an input text box in the website itself.
#def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/privacy-policy')
def privacyPolicy():
    return render_template('privacyPolicy.html')



#take input from the input text box and return the predicted text
@app.route('/inputData', methods=['GET', 'POST'])
def inputText():
    data = request.get_json()  #get data from the user
    input_text = TextFile()    # instantiate an object of TextFile
    assert isinstance(input_text, TextFile)
    predicted_text = input_text.PredictText(data['x'])
    #print(predicted_text)
    return jsonify({'result': predicted_text})  # return the predicted text back to the html page.


#take user facebook posts and return the predicted facebook posts
@app.route('/facebookData', methods=['GET', 'POST'])
def getFBArray():
    data = request.get_json()
    fbpost = facebookPosts()   # instantiate an object of facebookPosts
    assert isinstance(fbpost, facebookPosts)
    predicted_text = fbpost.PredictText(data)
    return jsonify({'result': predicted_text})


#take user tweets and return the predicted tweet
@app.route('/twitterData', methods=['GET', 'POST'])
def getTwitterData():
    data = request.get_json()
    tweets = twitter()   # instantiate an object of twitter
    assert isinstance(tweets, twitter)
    predicted_text = tweets.PredictText(data)
    return jsonify({'result': predicted_text})


if __name__ == '__main__':
    app.run('0.0.0.0')