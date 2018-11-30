from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from flask_pymongo import PyMongo
import bcrypt

#changes
app = Flask(__name__, instance_relative_config=True)
app.config['MONGO DBNAME'] = 'bobcatbaazar'
app.config['MONGO_URI'] = 'mongodb://bobcat:bobcat2018@ds127843.mlab.com:27843/bobcatbaazar'

mongo = PyMongo(app)



@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        user = mongo.db.users
        login_user = user.find_one({'NetId': request.form['netid']})
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['Password']) == login_user['Password']:
                session['username'] = request.form['netid']
                uname = login_user['First Name']
                return redirect(url_for('home', username=uname))
        error = 'Invalid Username or password combination'
        return render_template('login1.html', error=error)
    return render_template('login1.html')

@app.route('/home/<username>')
def home(username):
    if 'username' in session:
        username = session['username']
        return render_template('home.html', uname=username)
    return "You are not logged in <br><a href='/'></b>" + \
            "click here to log in</b></a>"

@app.route('/buy')
def buy():
    if 'username' in session:
        username = session['username']
        return render_template('buy.html')
    return "You are not logged in <br><a href='/'></b>" + \
           "click here to log in</b></a>"

@app.route('/sell',  methods=['POST','GET'])
def sell():
    if request.method == 'POST':
        Sell_Book = mongo.db.Sell_Books
        college = request.form['college']
        department = request.form['department']
        b_name = request.form['BookName']
        course_id = request.form['CourseId']
        pay_method = request.form['pay_method']
        price = request.form['Price']
        netid = session['username']
        Sell_Book.insert({'NetId': netid, 'College': college, 'Department': department, 'Book Name': b_name, 'Course_ID': course_id, 'Pay_Type': pay_method, 'Price': price})
        return redirect(url_for('sell'))
    return render_template('sell.html')

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        return render_template('profile.html')
    return "You are not logged in <br><a href='/'></b>" + \
           "click here to log in</b></a>"

@app.route('/messages')
def messages():
    if 'username' in session:
        username = session['username']
        return render_template('messages.html')
    return "You are not logged in <br><a href='/'></b>" + \
           "click here to log in</b></a>"

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route('/register', methods =['GET','POST'])
def register():
    if request.method == 'POST':
        user = mongo.db.users
        existing_users = user.find_one({'NetId': request.form['netid']})
        if existing_users is None:
            password = request.form['password']
            fname = request.form['Fname']
            lname = request.form['Lname']
            netid = request.form['netid']
            pw_hash = bcrypt.hashpw((password).encode('utf-8'), bcrypt.gensalt())
            user.insert({'First Name': fname, 'Last Name': lname, 'NetId': netid, 'Password': pw_hash})
            return redirect(url_for('index'))
        return 'That username already exist'
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)




