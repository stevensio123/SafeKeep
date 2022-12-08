import functools
import random
import string

from flask import Blueprint, flash ,redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from . import auth
from .. import db
from ..forms import LoginForm, RegistrationForm
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            print('logged in!')
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid Username or Password')
    return render_template('login.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    name=form.name.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/pgenerator', methods=['GET', 'POST'])
def pgenerator():
    if request.method == "POST":
        #print(string.printable)
        char_seq = string.printable
        #print(char_seq)
        
        length = int(request.form.get("length"))
        password = ''
        
        if length >= 8 and length <= 16:
            
            #generate random chars with "length" amount of times, add chars together to form password
            for len in range(length):
                random_char = random.choice(char_seq)
                password += random_char
                
            #reshuffle the list of chars in the generated password 
            list = list(password)
            random.shuffle(list)
            final_password = ''.join(list)
            return render_template('pgenerator.html',pasword=final_password)
    
    else:
        length = 13
        password = ''
        char_seq = string.printable
        #generate random chars with "length" amount of times, add chars together to form password
        for len in range(length):
            random_char = random.choice(char_seq)
            password += random_char
            
        #reshuffle the list of chars in the generated password 
        list = list(password)
        random.shuffle(list)
        final_password = ''.join(list)
    return render_template('pgenerator.html',pasword=final_password)



