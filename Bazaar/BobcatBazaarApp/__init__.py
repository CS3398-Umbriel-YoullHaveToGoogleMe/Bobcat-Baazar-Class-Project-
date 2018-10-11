from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/')
def login():
    return render_template('login.html')
