from flask import Flask, render_template, url_for, flash, redirect
from Bazaar_App import app
from Bazaar_App.forms import RegistrationForm, LoginForm

@app.route('/hello')
def hello():
	return render_template('hello.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		return '<h1>Registration Form validated</h1>'
		"""user = mongo.db.users
		existing_users = user.find_one({'NetId': form.netID.data})
		if existing_users is None:
			password = form.password.data
			fname = form.firstname.data
			lname = form.lastname.data
			netid = form.netID.data
			pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
			user.insert({'First Name': fname, 'Last Name': lname, 'NetId': netid, 'Password': pw_hash})
			return redirect(url_for('login'))"""
	return render_template('register.html', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return '<h1>Login form validated</h1>'
		"""user = mongo.db.users
		login_user = user.find_one({'NetId': form.netID.data})
		if login_user is None:
			return '<h1>User is None!</h1>'
		if login_user:# and bcrypt.check_password_hash(login_user['Password'], form.password.data):
			return '<h1>Login Validated!</h1>'
			session.clear()
			session['username'] = form.netID.data
			username = login_user['First Name']
			return redirect(url_for('hello', username=username))"""
	return render_template('login.html', form=form)