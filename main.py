from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
import markovify

from flask import Flask

from MainTemplate import MainTemplate
from facebookPosts import facebookPosts

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


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            #return  # redirect(request.url)
            return "This functionality is yet to be implemented."
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            #return  # redirect(request.url)
            return "This functionality is yet to be implemented."
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("KAW")
            #return  # redirect(url_for('uploaded_file', filename=filename))
            return "This functionality is yet to be implemented."
    return '''

    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/list', methods=['GET', 'POST'])
def getFBArray():
    data = request.get_json()
    #return jsonify({'result': "TEST POST PLEASE IGNORE"})
    # x = data['x']
    # print(x)
    fbpost = facebookPosts()
    assert isinstance(fbpost, facebookPosts)
    predicted_text = fbpost.PredictText(data)
    # print(predicted_text)
    return jsonify({'result': predicted_text})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
