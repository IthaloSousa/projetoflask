from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from sqlalchemy import true
from app import app, db
from app.models import User
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import re

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        usuario = request.form['usuario']

        user = User(name, email, pwd, usuario)
        db.session.add(user)
        db.session.commit()
        
    return render_template('register.html')


@app.route('/existente')
def existente():
    return render_template('existe.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('negado'))        

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/negado', methods=['GET', 'POST'])
def negado():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('negado'))        

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login_two.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

app.run(debug=True)