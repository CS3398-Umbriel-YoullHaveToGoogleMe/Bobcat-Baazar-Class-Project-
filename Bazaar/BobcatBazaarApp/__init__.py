from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, instance_relative_config=True)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/', methods=['POST','GET'])
def login_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

#@app.route('/register')
#def buy():
#	return render_template('register.html')