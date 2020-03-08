from flask import Flask, render_template, request, url_for, redirect, session
from flask_mysqldb import MySQL
from flask_hashing import Hashing

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'admin_db'
mysql = MySQL(app)
hashing = Hashing(app)

app.secret_key = "Hell0"

# @app.route('/')
# def home():
# 	password ='12341234'
# 	passhash = hashing.hash_value(password, salt='abcd')
# 	return passhash
# 	#return redirect(url_for('login'))

@app.route('/login')
def login():
	userLogAccess = session.get('userLogAccess', 'FALSE')
	if userLogAccess != 'FALSE':
		return redirect('dashboard')
	else:
		return render_template('user_login.html')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('login')

@app.route('/auth', methods=['POST'])
def auth():
	username = request.form['username']
	password = request.form['password']

	# username = '15.11.8815'
	# password = '12341234'

	passhash = hashing.hash_value(password, salt='abcd')
	cur = mysql.connection.cursor()
	cur.execute("SELECT user_password FROM user WHERE user_email = %s",(username,))
	mysql.connection.commit()

	dataAuth = cur.fetchall()

	countAuth = int(len(dataAuth))
	if countAuth == 1:

		n = 0
		[x[n] for x in dataAuth]
		for row in dataAuth:
			passwordLibrarian = row[n]


		if passhash == passwordLibrarian:
			session['userLogAccess'] = username
			return redirect('books')

		else:
			return 'Password false!!!'
			
	else:
		return 'Username ont found!!!'
	
# @app.route('/dashboard')
# def dashboard():
# 	pass:


if __name__ == '__main__':
	app.run(debug=True)