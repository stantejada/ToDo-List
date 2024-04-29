from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email='email').first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
                
            else:
                flash('Incorrect password!', category='error')
        else:
            flash('Username doesn\'t exist!', category='error')
    
    return render_template('login.html', user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#is a decorator used to know the path and method
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    
    if request.method == 'POST':
        #get the data sendding from forms of sign-up
        email = request.form.get('email')
        password = request.form.get("password")
        password2 = request.form.get('password2')
        
        
        user = User.query.filter_by(email='email').first()
        
        #show massage of error or success in order to everything is correct
        if user:
            flash('User already exists!', category='error')
        elif len(email) < 8:
            flash('Email must be greater than 8 characters', category='error')
        elif password != password2:
            flash('Password don\'t match', category='error')
        elif len(password) < 8:
            flash('Password must be greater than 8 character', category='error')
        else:
            #create new user and send data to our database
            new_user = User(email = 'email', password = generate_password_hash(password, method='pbkdf2:sha256')  )
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account has been created succesfully!', category='success')
            
            return redirect(url_for('views.home'))
            
    #return the template.html 
    return render_template('signup.html', user= current_user)