from flask import Flask, render_template, url_for, flash, redirect, session
from Bazaar_App import app, mongo, bcrypt
from Bazaar_App.forms import RegistrationForm, LoginForm, SellForm

@app.route('/hello')
def hello():
	return render_template('hello.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.is_submitted():
		print('submitted')
	if form.validate_on_submit():
		#return '<h1>Registration Form validated</h1>'
		user = mongo.db.users
		existing_users = user.find_one({'NetId': form.netID.data})
		if existing_users is None:
			password = form.password.data
			fname = form.firstname.data
			lname = form.lastname.data
			netid = form.netID.data
			pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
			user.insert({'First Name': fname, 'Last Name': lname, 'NetId': netid, 'Password': pw_hash})
			return redirect(url_for('login'))
	return render_template('register.html', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.is_submitted():
		print('submitted')
	if form.validate_on_submit():
		#return '<h1>Login form validated</h1>'
		user = mongo.db.users
		login_user = user.find_one({'NetId': form.netID.data})
		if login_user is None:
			return '<h1>User is None!</h1>'
		if login_user and bcrypt.check_password_hash(login_user['Password'], form.password.data):
			#return '<h1>Login Validated!</h1>'
			session.clear()
			session['username'] = form.netID.data
			username = login_user['Last Name']
			return redirect(url_for('home', username=username))
	return render_template('login_temp.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	return redirect(url_for('login'))

@app.route('/home/<username>', methods=['GET', 'POST'])
def home(username):
	return render_template('home.html', username=username)

@app.route('/buy/<username>', methods=['GET', 'POST'])
def buy(username):
	return render_template('buy.html', username=username)

@app.route('/sell/<username>', methods=['GET', 'POST'])
def sell(username):
	form = SellForm()
	if form.is_submitted():
		print('submitted')
	if form.validate_on_submit():
		#return '<h1>Sell Form validated</h1>'
		return redirect(url_for('buy', username=username))
	return render_template('sell.html', username=username, form=form)

@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
	return render_template('profile.html', username=username)

@app.route('/messages/<username>', methods=['GET', 'POST'])
def messages(username):
	return render_template('messages.html', username=username)