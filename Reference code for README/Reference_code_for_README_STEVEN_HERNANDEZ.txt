*************************************************************************************************

	This is the code that I contributed for Sprint 3 from __init__.py and buy.html

*************************************************************************************************

----------------------------------------------------------------------------------------------------
All methods in __init__.py so that user cannot access unless logged in (except index and register):
----------------------------------------------------------------------------------------------------

   if request.method == 'POST' and 'username' in session:


   elif 'username' not in session:
   	return redirect(url_for('index'))


-----------------------------------------------------------------------------------------------------
buy method in __init__.py to search for all books in database that match search terms and pass them:
-----------------------------------------------------------------------------------------------------

    if request.method == 'POST' and 'username' in session:
        username = session['username']
        college = request.form['college']
        department = request.form['department']
        courseId = request.form['CourseId']
        books = mongo.db.Sell_Books
        results = list(books.find( {'$and':[{'College': college}, {'Department': department}, {'Course_ID': courseId}]}))
        return render_template('buy.html', results=results)


-------------------------------------------------------------------------------
register method in __init__.py to add confirm password field to register page:
-------------------------------------------------------------------------------

	confirm_password = request.form['confirm_password']
            if confirm_password != password:
                error = 'Password must match'
                return render_template('register.html', error=error)

----------------------------------------------
additions to both buy.html and register.html:
----------------------------------------------

<div class="wrap-input100 validate-input" data-validate="Password is required">
						<span class="label-input100">Confirm Password</span>
						<input class="input100" type="password" name="confirm_password" placeholder="Confirm Password" required>
						<span class="focus-input100" data-symbol="&#xf190;"></span>
					</div>

{% for book in results %}
				     <tr>
						 <td>{{ book['Book Name'] }}</td>
						 <td>{{ book['Course_ID'] }}</td>
						 <td>{{ book['Department'] }}</td>
					 </tr>
				  {% endfor %}