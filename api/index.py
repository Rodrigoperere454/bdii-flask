from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!- BD2 10/03/2025'

@app.route('/about')
def about():
    return 'About'