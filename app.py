from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from models import login_auth, get_all_users

import hashlib

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SESSION_PERMANTENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/')
def index():
    return 'hello world'


@app.route('/admin')
def admin_dashboard():
    return render_template('Admin/index.html')


@app.route('/admin/users')
def admin_users():
    users = get_all_users()
    return render_template('Admin/Users/index.html', users=users)


@app.route('/admin/login', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        email_address = request.form['email_address']
        password = request.form['password']

        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))

        result = login_auth(email_address, md5.hexdigest())
        if result:
            session['name'] = result['name']
            session['email_address'] = result['email_address']
            session['user_level'] = result['user_level']
            return redirect('/admin')
        else:
            return render_template('login.html', error='Invalid email or password')
    return render_template('login.html')


@app.route('/admin/logout')
def admin_logout():
    session['name'] = None
    session['email_address'] = None
    session['user_level'] = None
    return redirect('/admin/login')


if __name__ == '__main__':
    app.run()
