from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
import markovify
import tweepy

from flask import Flask

from MainTemplate import MainTemplate
from facebookPosts import facebookPosts
from textFile import TextFile

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/privacy-policy')
def privacyPolicy():
    return render_template('privacyPolicy.html')


@app.route('/inputData', methods=['GET', 'POST'])
def inputText():
    data = request.get_json()
    #return jsonify({'result': "TEST POST FOR TEXT INPUT PLEASE IGNORE"})
    input_text = TextFile()
    assert isinstance(input_text, TextFile)
    predicted_text = input_text.PredictText(data['x'])
    print(predicted_text)
    return jsonify({'result': predicted_text})


@app.route('/facebookData', methods=['GET', 'POST'])
def getFBArray():
    data = request.get_json()
    #return jsonify({'result': "TEST POST FOR FACEBOOK PLEASE IGNORE"})
    # x = data['x']
    # print(x)
    fbpost = facebookPosts()
    assert isinstance(fbpost, facebookPosts)
    predicted_text = fbpost.PredictText(data)
    # print(predicted_text)
    return jsonify({'result': predicted_text})

@app.route('/twitterData', methods=['GET', 'POST'])
def getTwitterData():
    data = request.get_json()

    auth = tweepy.OAuthHandler("t1lQX1VkiCf3dHC4z9XOtf8wy", "rh2KjvPIakeymfrMzQYXtR5T3AFYB3Rt1yq4ZW2YcL5Eji2EpI")
    auth.set_access_token("72186647-4qqJpl6DpSKEqVhDsLxQjmqTcq8YyoRwl1ow2xaZG", "q9SsVA3v8BJSFqZKrEAErbJMmfM3VzNRCLiWf0DVJTNkm")
    twitter_api = tweepy.API(auth)
 
    if (data['user1'] != ''):
        getUser1Tweets = tweepy.Cursor(twitter_api.user_timeline, id = data['user1']).items(5)
        for result in getUser1Tweets:
            print(result.text)

    if (data['user2'] != ''):
        getUser2Tweets = tweepy.Cursor(twitter_api.user_timeline, id = data['user2']).items(5)
        for result in getUser2Tweets:
            print(result.text)

    return result.text


if __name__ == '__main__':
    app.run()

