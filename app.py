from flask import Flask, render_template, json, url_for, redirect, session, request
import redis

from flask_mysqldb import MySQL
app = Flask(__name__)

host = "127.0.0.1"
port = 6379
password = ""


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)



@app.route('/login', methods=['GET', 'POST'])
def login():

    msg = ''

    if request.method == 'POST' and 'studentId' in request.form and 'studentPassword' in request.form :
        username = request.form['studentId']
        password = request.form['studentPassword']


        cursor.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM student WHERE student_id = %s AND student_password = %s', (username, password))

        account = cursor.fetchone()
        if account:
            session['loggedin'] = 'True'
            session['id'] = account['id']
            session['name'] = account['name']

            return 'Login success'
        else:
            msg = 'Incorrect username / password'


    else:
        return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
