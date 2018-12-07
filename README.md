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


To view the front end of the application.
To view the HTML files created. Navigate to "HTML files" folder

To view the database files of our applictiion.
Navigate to Bobcat_Bazaar/flaskr/BobcatBazaar1.sql


Sprint 3:

  Nabil Manasiya :
- I created the table on the sell page that works as a results table from the user search for a book. 
  The idea behind the results table was to present users with a simple yet organized way to see their output of books. 
  There was a part were my team mate steven hernandez helped me in organizing the data within the tables.
- I also worked on adding logic to the drop down menus on buy and sell page. In our previous sprint we had our drop downs
  present us with fields that were same for all of the colleges and departments, but this time i made the department drop
  down depend on the college drop down making it change according to the user’s selection of college.
- My code/artifact file that this readme is refering to could be found on the master brance, it is a text file which is named
  Reference_code_for_README_NABIL_MANASIYA.txt. This file contains code that is used in our sell.html page and buy.html page.
  This code is one of the many key features that we have in our project.
- As far as measurable improvements are concerned, in sprint 2 i implemented the drop downs but they were without the logic and
  not so very well designed, but in sprint 3 i made a significant improvement and made progress on it. You can see how the drop
  down looks now.
  
 Aadil Khatri:
- I created a table/data for books in MongoDb, that works as a user wants to sell a book, that book will be stored in to the 
database table called Sell_Books. Also, if a user wants to buy a book and wants to search for a book, he/she will be able to get 
the results if there are any with a book name, college, department, Course ID, for the book through the database.
- My code/artifact file that this readme is referring to could be found on the master branch, it is a text file which is named 
Reference_code_for_readme_Aadil_Khatri_.txt. This file contains code that is used in our sell.html page and buy.html page. 
This This is used at buying, selling and searching for a book.
- For the measurable improvements, in sprint 2 I was kind of behind in handling the ZenHub board and not being able to move the tasks at
the right time. Also in sprint 2, I wasn't able to commuicate effectively with the backend as I should have. But in sprint 3 I was able
sit down with the backend and talk effectively about how the database is going to work and what the tables are going to be used for. 
In sprint 3 I was able to keep up with the tasks on ZenHub. In previous sprints there were some errors that I made while I was making 
the user table, but in this sprint I made sure not to make those errors on the book table hence I have improved on that part as you can 
see the code and the working program.

 Steven Hernandez:
- I added code to utilize user sessions in flask in order to prevent users of the website from accessing certain pages without being logged in first. This code can be seen in all of the methods in __init__.py except for the index and register methods since those pages do not require login.
- I added code to the buy method in __init__.py to take the search terms entered by the user in the buy.html page and query the database for all books that match those search terms.  Once that list is compiled, that list is then returned back to the html page for displaying the results to the user. (Lines 36 - 42 of __init__.py)
- I added a few lines of code to the register function in __init__.py to implement a confirm password field on the register page. (Line 90 - 93 of __init__.py)
- I added a few lines to register.html to add the confirm password field. (Lines 61 - 65 of register.html)
- I added a few lines to buy.html to add the results of the search query into the table that Nabil designed. (Lines 205 - 211 of buy.html)
- My code/artifact file that this readme is refering to could be found on the master brance, it is a text file which is named
  Reference_code_for_README_STEVEN_HERNANDEZ.txt. This file contains code that is used in our buy.html page and our back-end file __init__.py.
- For this sprint, I was able to improve how I handled the ZenHub board.  This time around I had the correct amount of hours assigned to myself.  I regularly looked at the board to make sure that it was an accurate representation of where I stood at that time.  I also did my best to make sure that it also accurately represented what my teammates were working on at the time.  You can see evidence of this by looking at what tasks were moved to the done column and what tasks remained in the In Progress column.  Everything in the done column can be found implemented or taken care of in our code.  Anything that remained in the In Progress column were really things that never got finished or implemented.

Salvador Romero: 
-I did research on how to implement sessions in the flask web framework. The actual implemintation of the sessions was done by Steven. 
-I also did reasearch on user email authentication. This would allow us to make the Bobcat Bazaar  only for Texas State students. At registration the user would be sent an email confirmation with a unique email sent to them. We would have to hardcode the email registration so that the domain would have to end with @txstate.edu. The student would have to confirm their email by clicking the link. Once they have clicked the link in the email their status would be set to confirmed. Now they will be able to sucessfuly log in. I was not able to implement this within our final sprint. 

Moiz Ahmed:
- I was tasked to crate the schema table and data for User table using MongoDB. Overall, when a user registers for an account the credentials are pushed to the "users" table successfully. These fields include fields such as first name, last name, netId and password. Making sure everything was being psuhed to the DB table properly and testing different conditions to see whether the data was not being lost under any circumstance. With these credentials, the user will also be able to login to their account.
- The artifact can be found under the "Reference code for README" folder under the name Reference_code_for_readme_Moiz_Ahmed_.docx. These are the data for the users in the database, and below are just of few from what I did, though in the DB there are 14 present in the database. users table for the MongoDB works directly with register.html and login.html and of course used for registering for an account and loggin in t your account.
- For Sprint 3 I was able to improve a whole lot. I kept up to date with the taskboard on zenhub to make sure everything is up to date and going as planned. This was not the case for me in the past previous 2 sprints. Unmeasurable improvements from me and all the other team members. I was also able to sit down with back end and confirm with them the final requirements and/or changes with the users table and the DB as a whole, and if there needed to be any improvements or changes in any way. Lastly, in previous sprint, the users table was not working as it should be, we were getting errors of various sorts (pushing and pulling). This sprint, I made sure the users table schema was optimized and working as it should with regards to storing, pushing, pulling, etc.
Salvador Romero: 
-I did research on how to implement sessions in the flask web framework. The actual implemintation of the sessions was done by Steven. 
-I also did reasearch on user email authentication. This would allow us to make the Bobcat Bazaar  only for Texas State students. At registration the user would be sent an email confirmation with a unique email sent to them. We would have to hardcode the email registration so that the domain would have to end with @txstate.edu. The student would have to confirm their email by clicking the link. Once they have clicked the link in the email their status would be set to confirmed. Now they will be able to sucessfuly log in. I was not able to implement this into our code. 


	
Back End Next Sprint:
(Steven Hernandez and Salvador Romero)
Main Goal: Combine front and back end.
and continue development.

We will need to learn more of the flask
web framework and get more familiar with it.
Learning how to replace the stock html pages 
that the Flask tutorial provided with our own 
html pages.

Front End Sprint 3 retropsective:
(Nabil Manasiya and Matt Stephens)
Nabil: Created the menu on the buy and sell pages. Deigned and implemented the login pages. (In the buy.html, sell.html, login1.html)
Matthew: Created site design and navigation. (added to all html files except the login1 file)
	For this sprint I checked in with my team on slack and met with nabil and the rest of the team after class mmore often than last 	sprint. I still should've been more actively communicating with my team.

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
