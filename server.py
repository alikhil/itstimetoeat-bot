from flask import Flask, send_file

from config import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/picture")
def picture():
    return send_file("pics/burger.jpg", mimetype='image/jpeg')

@app.route("/labeled-picture")
def labaled_picture():
    return send_file("pics/food.jpg", mimetype='image/jpeg')

@app.route("/predict")
def predict():
    return "There is fucking big queue now. Don't go there if you don't want to waste your time"

if __name__ == '__main__':
    app.run()