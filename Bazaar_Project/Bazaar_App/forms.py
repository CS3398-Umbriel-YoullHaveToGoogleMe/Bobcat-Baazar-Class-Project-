from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
	firstname = StringField('Firstname',
							validators=[DataRequired(), Length(min=2, max=20)])
	lastname = StringField('Lastname',
							validators=[DataRequired(), Length(min=2, max=20)])
	netID = StringField('netID',
						validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
									 validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	netID = StringField('netID',
						validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	#remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class SellForm(FlaskForm):
	book_name = StringField('Book Name',
							validators=[DataRequired()])
	book_description = StringField('book Description',
							validators=[DataRequired()])
	price = StringField('Price',
						validators=[DataRequired()])
	college = SelectField('College',
						choices=[('CS', 'Computer Science'), ('MIS', 'MIS'),
								 ('EN', 'Engineering'), ('MATH', 'Mathematics')])
	submit = SubmitField('Post')