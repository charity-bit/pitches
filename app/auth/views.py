from flask import flash, redirect, render_template, url_for,request
from flask_login import login_required, login_user, logout_user
from ..models import User
from .. import db

from .forms import RegistrationForm
from . import auth
from flask import render_template

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/register',methods = ['GET','POST'])
def register():
    rform = RegistrationForm()
    print(rform)
    if rform.validate_on_submit():
        user = User(username = rform.username.data,email= rform.email.data,password = rform.password.data)
        user.save_user()
        print(user)
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html',rform = rform)


