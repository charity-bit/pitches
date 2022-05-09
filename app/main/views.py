

from crypt import methods
from os import path
from flask import redirect, render_template, request, url_for,flash,abort
from flask_login import login_required,current_user
from . import main
from ..models import Pitch,User
from .. import db,photos


@main.route('/')
def index():
    pitches =  Pitch.query.all()
    return render_template('index.html',pitches = pitches)

@main.route('/post-pitch',methods = ['GET','POST'])
@login_required
def post():
    if request.method == 'POST':
        title = request.form.get('title')
        pitch = request.form.get('pitch') 
        category =  request.form.get('category')
        user_id = current_user._get_current_object().id
        pitch= Pitch(title = title,category = category,content= pitch,user_id = user_id)
        pitch.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('post.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user = user)

@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        photo = photos.save(request.files['photo'])
        f_path = f'photos/{photo}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',uname = uname))

@main.route('/user/<uname>/edit',methods=['GET','POST'])
@login_required
def edit_profile(uname):
    user = User.query.filter_by(username = uname).first()
    return render_template('/profile/edit.html',user = user)
    








