from flask import flash, redirect, render_template, url_for,request
from flask_login import current_user, login_required, login_user, logout_user


from ..models import User
from .. import db

from .forms import LoginForm, RegistrationForm
from . import auth
from flask import render_template

@auth.route('/login',methods = ['GET','POST'])
def login():
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        if user is not None and user.verify_password(lform.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('auth/login.html',lform = lform)

@auth.route('/register',methods = ['GET','POST'])
def register():
    rform = RegistrationForm(request.form)
    print(rform)
    if rform.validate_on_submit():
        user = User(username = rform.username.data,email= rform.email.data,password = rform.password.data)
        user.save_user()
        login_user(user)
        print(user)
        
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html',rform = rform)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

