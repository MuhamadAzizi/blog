from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from werkzeug.utils import secure_filename
from models import login_auth, get_all_users, add_user, delete_user, get_user_by_id, update_user, get_all_articles

import os
import hashlib

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SESSION_PERMANTENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Session(app)


@app.route('/')
def index():
    return 'hello world'


@app.route('/admin')
def admin_dashboard():
    return render_template('Admin/index.html')


@app.route('/admin/articles')
def admin_articles():
    articles = get_all_articles()
    return render_template('Admin/Articles/index.html', articles=articles)


@app.route('/admin/users')
def admin_users():
    users = get_all_users()
    return render_template('Admin/Users/index.html', users=users)


@app.route('/admin/users/add', methods=['POST'])
def admin_users_add():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email_address = request.form['email_address']
        password = request.form['password']
        user_level = request.form['user_level']
        add_user(id, name, email_address, password, user_level)
        return redirect('/admin/users')


@app.route('/admin/users/<id>')
def admin_users_id(id):
    user = get_user_by_id(id)
    return render_template('Admin/Users/update.html', user=user)


@app.route('/admin/users/<id>/update', methods=['POST'])
def admin_users_update(id):
    if request.method == 'POST':
        name = request.form['name']
        email_address = request.form['email_address']
        password = request.form['password']
        user_level = request.form['user_level']
        update_user(id, name, email_address, password, user_level)
        return redirect('/admin/users')


@app.route('/admin/users/delete/<id>')
def admin_users_delete(id):
    delete_user(id)
    return redirect('/admin/users')


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
