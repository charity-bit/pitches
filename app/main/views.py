from flask import redirect, render_template, request, url_for,flash,abort
from flask_login import login_required,current_user
from . import main
from ..models import DownVote, Pitch,User,Comment,UpVote
from .. import db,photos


@main.route('/')
def index():
  
    all =  Pitch.query.all()
    rev = all[::-1]

    return render_template('index.html',all = rev)



@main.route('/pitches/pickup-lines')
def pick():
    pick = Pitch.query.filter_by(category = 'Pick Up lines').all()
    rev = pick[::-1]
    return render_template('pick.html',pick = rev)



@main.route('/pitches/promotion')
def promotion():
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    rev = promotion[::-1]
    return render_template('promotion.html',promotion = rev)



@main.route('/pitches/comedy')
def comedy():
    comedy = Pitch.query.filter_by(category = 'Comedy').all()
    rev = comedy[::-1]
    return render_template('comedy.html',comedy = rev)


@main.route('/pitches/product-pitch')
def product_pitch():
    product = Pitch.query.filter_by(category = 'Product Pitch').all()
    rev = product[::-1]
    return render_template('product.html',product = rev)



@main.route('/pitches/interview')
def interview():
    interview = Pitch.query.filter_by(category = 'Interview').all()
    rev = interview[::-1]
    return render_template('interview.html',interview = rev)



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


@main.route('/comment/<int:pitch_id>',methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    comments = Comment.query.filter_by(pitch_id = pitch_id)
    user_id = current_user._get_current_object().id
    pitch = Pitch.query.get(pitch_id)
    if request.method == 'POST':
        comment = request.form.get('comment')
        new_comment = Comment(comment = comment , pitch_id = pitch_id,user_id = user_id)
        new_comment.save_comment()
        return redirect(url_for('main.comment',pitch_id = pitch_id))

    return render_template('comment.html',comments = comments,pitch = pitch)



@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    pitches = Pitch.query.filter_by(user_id = user_id).all()
    rev = pitches[::-1]
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user = user,pitches = rev)



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
        emailf = User.query.filter_by(email = email).first()
        if usernamef and usernamef is not user.username:
            
            username =  user.username 
            flash('that username is taken')

        
        if emailf and emailf is not user.email:
            email = user.email 
            flash('that email is taken')
            
        
        user.email = email
        user.username = username
        user.bio = bio
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))
    return render_template('/profile/edit.html',user = user)


@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def upvote(id):
    pitch = Pitch.query.get(id)
    new_vote = UpVote(pitch = pitch,upvote = 1)
    new_vote.save_upvote()
    return redirect(url_for('main.index'))
           
    
    

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def downvote(id):
    pitch = Pitch.query.get(id)
    new_vote = DownVote(pitch = pitch,downvote = 1)
    new_vote.save_downvote()
    return redirect(url_for('main.index'))
           
           

     

    








