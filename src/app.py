from flask import Flask

__author__ = "Prajesh Ananthan"

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello_world():
    return "Hello World"