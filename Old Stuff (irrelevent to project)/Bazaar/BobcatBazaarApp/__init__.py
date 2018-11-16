import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from werkzeug.security import check_password_hash, generate_password_hash
from BobcatBazaarApp.db import get_db

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'BobcatBazaarApp.sqlite'),
)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from . import db
db.init_app(app)

@app.route('/hello')
def hello():
    return 'Hello World!'
#default place the webpage will go to when we first start it up
@app.route('/')
def login():
    return render_template('login.html')
#log in page will pop up when we first load the program too.
#the page is of form POST becasue we will wwant to get the user input 
#to store in the database like username and password.
@app.route('/', methods=['POST','GET'])
def login_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['username']
            return redirect(url_for('home'))

        flash(error)

    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/logout')
def logout_post():
    session.clear()
    time.sleep(2)
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')
@app.route('/sell')
def sell():
    return render_template('sell.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST', 'GET'])
def register_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('login'))

        flash(error)

    return render_template('register.html')

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE username = ?', (user_id,)
        ).fetchone()