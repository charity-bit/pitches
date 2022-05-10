
from flask import redirect, render_template, request, url_for,flash,abort
from flask_login import login_required,current_user
from . import main
from ..models import Pitch,User
from .. import db,photos


@main.route('/')
def index():
  
    all =  Pitch.query.all()
    return render_template('index.html',all = all)

@main.route('/pitches/pickup-lines')
def pick():
    pick = Pitch.query.filter_by(category = 'Pick Up lines').all()
    return 'pick up'

@main.route('/pitches/promotion')
def promotion():
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    return 'product promotion'



@main.route('/pitches/comedy')
def comedy():
    comedy = Pitch.query.filter_by(category = 'Comedy').all()
    interview = Pitch.query.filter_by(category = 'Interview').all()
    return 'comedy'


@main.route('/pitches/product-pitch')
def product_pitch():
    product = Pitch.query.filter_by(category = 'Product Pitch').all()
    return 'product pitch'

@main.route('/pitches/interview')
def interview():
    interview = Pitch.query.filter_by(category = 'Interview').all()
    return 'intervies'



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
@main.route('/comment/<int:post_id>' , methods = ['GET','POST'])
@login_required
def comment(post_id):
    return 'comment'

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    pitches = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user = user,pitches = pitches)

@main.route('/user/<uname>/edit/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        photo = photos.save(request.files['photo'])
        filename= f'photos/{photo}'
        user.pic_path = filename
        db.session.commit()

    return redirect(url_for('main.profile',uname = uname))

@main.route('/user/<uname>/edit',methods=['GET','POST'])
@login_required
def edit_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        bio = request.form.get('bio')

        usernamef = User.query.filter_by(username = username).first()
        if usernamef and usernamef != user.username:
            flash('user already exists')

        emailf = User.query.filter_by(email = email).first()
        if emailf and emailf != user.email:
            flash('Email already exists')

        user.email = email
        user.username = username
        user.bio = bio
        
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))
    return render_template('/profile/edit.html',user = user)
    








