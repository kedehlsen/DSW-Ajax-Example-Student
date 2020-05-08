from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template

app = Flask(__name__)

app.debug = True #Change this to False for production

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hidden-message')
def hidden_message():
    return Markup('<p>This is the hidden message!</p> <h2>This is a new title</h2>')
if __name__ == '__main__':
    app.run()
