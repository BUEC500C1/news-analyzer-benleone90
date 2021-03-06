from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os

application = Flask(__name__)

application.secret_key = 'random_key'

DEV = False
if DEV == True:
    application.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
    application.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
    application.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
    application.config['MYSQL_DB'] = 'newsanalyzer'
elif DEV == False:
    application.config['MYSQL_HOST'] = os.environ['RDS_HOSTNAME']
    application.config['MYSQL_USER'] = os.environ['RDS_USERNAME']
    application.config['MYSQL_PASSWORD'] = os.environ['RDS_PASSWORD']
    application.config['MYSQL_DB'] = os.environ['RDS_DB_NAME']

mysql = MySQL(application)


@application.route('/')
@application.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM auth WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully!'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username or password'
    return render_template('login.html', msg=msg)


@application.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@application.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM auth WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password:
            msg = 'Please fill out the form!'
        else:
            cursor.execute(
                'INSERT INTO auth VALUES (NULL, % s, % s)', (username, password, ))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)


if __name__ == '__main__':
    application.run(debug=True)
