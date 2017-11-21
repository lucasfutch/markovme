from flask import Flask, render_template, request, redirect, url_for, send_from_directory
# import requests


from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list', methods=['GET', 'POST'])
def getFBArray():
   	data = request.get_json()
	x = data['x']
	print x
   	return "Data in Python"



    # return jsonify(result=wordlist)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)