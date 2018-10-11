# Bobcat-Baazar-Class-Project-
Things to have before starting:
python 3.6 
Flask for python installed. 

Clone the git repository into a desired location.

To run the backend of the application:
Do the commands in the terminal or cmd.
	
	For linux and Mac:
	export FLASK_APP = flaskr
	flask init-db
	export FLASK_ENV=development
	flask run.

	For Windows:
	set FLASK_APP=flaskr
	set FLASK_ENV=development 
	flask run 

	The output of should look something like this
	Make sure the evniorment is set to development 
	instead of production
	Succesful launch will look like this
	* Serving Flask app "flaskr"
	* Environment: development
	* Debug mode: on
	* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
	* Restarting with stat
	* Debugger is active!
	* Debugger PIN: 855-212-761

	Open up your desired web browser and enter
	http://127.0.0.1:5000

	This should lead you to a page that has "Hello World" displayed
	to get to the register page add /auth/register
	http://127.0.0.1:5000/auth/register

	type username and password
	click register
	it will take you to the log in page
	use the credentials of the account created
	and hit log in
	it should take you the post page.

To veiw the front end of the application.
To view the HTML files created. Navigate to "HTML files" folder

To view the database files of our applictiion.
Navigate to Bobcat_Bazaar/flaskr/BobcatBazaar1.sql

	
Back End Next Sprint:
(Steven Hernandez and Salvador Romero)
Main Goal: Combine front and back end.
and continue development.

We will need to learn more of the flask
web framework and get more familiar with it.
Learning how to replace the stock html pages 
that the Flask tutorial provided with our own 
html pages.

Front End Next Sprint:
(Nabil Manasiya and Matt Stephens)
Main Goal: Make HTML pages more interactive and user
friendly by adding appropriate components and design to it.
Research and insert appropraite javascript to make 
HTML pages interact with the back end code.
Learn about Jinja2 templates which will help us 
render our data from back end to the front end and vice versa. 

	