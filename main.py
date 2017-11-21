from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

#from flask import Flask


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
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''

    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/list', methods=['GET', 'POST'])
def getFBArray():
   	data = request.get_json()
	x = data['x']
	print(x)
   	return "Data in Python"



    # return jsonify(result=wordlist)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)