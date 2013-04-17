from flask import Flask, json
app = Flask(__name__)

import datetime

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user(username):
    date = str(datetime.datetime.now())
    tmp = username+date
    return json.JSONEncoder().encode([date,username])

if __name__ == '__main__':
    app.run(debug=True)