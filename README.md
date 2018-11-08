ls
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
Main Goal:For the next sprint we have to complete our basic requirements for our HTML pages such as, all the textboxes or labels
that we need should be in place. Some of the HTML pages such as BUY and SELL should also be ready and designed completly. We are
plannign to add all the necessary javascript to our files as our back end requires us to do.

Back End Final Sprint:
(Steven Hernandez and Salvador Romero)
Main Goal: Finish routing all of the pages together. 
Set up sessions so that we can keep track of users information during 
the time they have logged in.

Implementing SOLID principles:
(discussion between team members)

Backend:
There is a way to devide the file containing the implementation of the backend into seperate files. We decided to keep everything in a single file since there is not much code needed to connect the backend with the front end. Once we add more to the file then we will need to revisit the question on how to devide the file. 

Front end:
For the front end we devided each page in our website into a different file.



	
