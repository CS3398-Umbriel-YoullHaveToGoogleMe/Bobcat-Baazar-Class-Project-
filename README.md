HOW TO RUN THE APPLICATION:
Also have to have python 3.6 installed to run this.
Before running the application make sure to have Flask,Flask_pymongo, and Bycrypt installed.

Python Flask Install Tutorial(Windows)
	http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/
Python Pymongo Install Tutorial (Windows)
	https://flask-pymongo.readthedocs.io/en/latest/
Installing Bypcrypt Tutorial for Bycrypt (Windows)
	https://www.npmjs.com/package/bcrypt

How to run Bobcat Bazaar Class Project.
	To run the project build and compile the __init__.py file. This should start running a web services on 127.0.0.1:5000
	From here you will be presented with our home page. To use the site you will need to register with a username and password of your choosing. To post book into the site go to the sell tab and fill out all the informatino for the book. To buy a book, go to buy tab and fill out the information for the book you are looking for. 


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

Database Final Sprint:
(Moiz Ahmed & Aadil Khatri)
Main Goal: the Database team will assess and understand any and all additional requirements/features and develop the database with all the required data structures. Also, we need to design a more robust database schema after consulting with back-end. After all that, we need to make it connect to back-end smoothly with out any problems.

Implementing SOLID principles:
(discussion between team members)

Backend:
There is a way to devide the file containing the implementation of the backend into seperate files. We decided to keep everything in a single file since there is not much code needed to connect the backend with the front end. Once we add more to the file then we will need to revisit the question on how to devide the file. 

Front end:
For the front end we devided each page in our website into a different file.


Revisted SOLID part of the program:
	To seperate our programs we went with one single back end page. We did this since all the functionality of the page is uniform throughout the code. Whenever we defien a button in an html page, we coded that button to ridirect to the appropriate page afterwards. We decided to seperate each of the html pages into their own files. When a link(button) is clicked in any of the web pages the back end page will load the new page up and this process will conitnue until the user decides to close the webpage. 