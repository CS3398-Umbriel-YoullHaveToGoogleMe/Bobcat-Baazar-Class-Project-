from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd79061b95c8940fdb4fd52a04e4b6241'
app.config['MONGO DBNAME'] = 'bobcatbaazar'
app.config['MONGO_URI'] = 'mongodb://bobcat:bobcat2018@ds127843.mlab.com:27843/bobcatbaazar'
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

from Bazaar_App import routes