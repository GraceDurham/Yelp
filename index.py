from flask import Flask 
from flask import render_template
from flask import request, url_for, redirect, session  
# import os 
# import sqlite3 


app = Flask(__name__)
# app.config.update(dict(DATABASE=os.path.join(app.root_path, 'phonebook.db')))

# def connect_db():
# 	rv = sqlite3.connect(app.config['DATABASE'])
# 	rv.row_factory =sqlite3.row
# 	return rv 

# def init_db():
# 	with app.app_context():
# 		db = get_db()
# 		with app.open_resource('schema.sql', mode='r') as f:
# 			db.cursor().executescript(f.read())
# 		db.commit()
		
# def get_db():
# 	if not hasattr(g, 'sqlite_db'):
# 		g.sqlite_db = connect_db()
# 	return g.sqlite_db

# @app.teardown_appcontext
# def close_db(error):
# 	if hasattr(g, 'sqilte_db'):
# 		g.sqilte_db.close()

	



@app.route("/")
def index():
	return "Welcome to the index page"

# @app.route("/")
# # def helloworld():
# # 	return "Hi How are you doing today? Hope you are doing well"


@app.route("/user/")
# def hellouser():
	#return "Hello User!"

@app.route("/user/")
@app.route("/user/<username>/")	
def welcomeuser(username=None):
	return render_template("hello.html", username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=='POST': 
		session['username']=request.form['username']   
		return redirect(url_for('welcomeuser', username=request.form["username"]))
	else:
		if 'username' in session:
			return 'Already logged in as %s. Please logout first' % session ['username']
		return render_template('login.html')

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
	return redirect(url_for('login'))		


app.secret_key = '1234'
if __name__ == '__main__':
	# init_db()
	app.run(debug=True)

