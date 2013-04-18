from flask import Flask, json
app = Flask(__name__)

import datetime
import numpy as np
from numpy import linalg as LA

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user(username):
    date = str(datetime.datetime.now())
    return json.JSONEncoder().encode([date,username])

@app.route('/inverse/<input>')
def show_inverse(input):
    mInit = [int(input[i]) for i in range(len(input))]
    matrix = np.matrix(mInit).reshape((3,3))

    return '<pre>' + str(LA.inv(matrix)) + '<pre>'

if __name__ == '__main__':
    app.run(debug=True)