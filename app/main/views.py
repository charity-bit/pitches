import re
from unicodedata import category
from flask import render_template, request
from flask_login import login_required,current_user
from . import main
from ..models import Post

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/post-pitch',methods = ['GET','POST'])
# @login_required
def post():
    if request.method == 'POST':
        title = request.form('title')
        pitch = request.form.get('pitch') 
        category =  request.form.get('category')
        




    return render_template('post.html')