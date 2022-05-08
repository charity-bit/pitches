from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin




# user
# fields  id,username,email,password 
# methods   saveuser, delete user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),nullable = False,unique = True)
    bio = db.Column(db.String(255))
    pic_path = db.Column(db.String(255))
    email = db.Column(db.String(255),nullable = False,unique = True)
    password = db.Column(db.String(255),nullable = False) 
    pitches = db.relationship('Pitch',backref = 'user',lazy = 'dynamic')
   
    


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot Read Attribute Error')

    @password.setter
    def password(self,password):
        self.password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return f'User: {self.username} {self.email}'


#  id(PK),title,category,pitch,user_id(FK),upvote(rl),downvote(rl),comment(rl)
# methods  => save_pitch,delete_pitch,view_all
class Pitch(db.Model):
    __tablename__ = 'pitches'



    id = db.Column(db.Integer,primary_key = True)
    title  = db.Column(db.String(255),nullable = False)
    category = db.Column(db.String(255),nullable = False)
    content = db.Column(db.String(255),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments  = db.relationship('Comment',backref = 'pitch',lazy = 'dynamic')
    upvotes = db.relationship('UpVote',backref = 'pitch',lazy = 'dynamic')
    downvotes = db.relationship('DownVote',backref = 'pitch',lazy = 'dynamic')
      


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def delete_pitch(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User: {self.content}'

class Comment(db.Model):

    __tablename__ = 'comments'

    id  = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(255), nullable = False)


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.add(self)
        db.session.commit()


        def __repr__(self):
            return f'User: {self.comment}'

class UpVote(db.Model):

    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key =True)
    upvote = db.Column(db.Integer,default = 0)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_upvote(self):
        db.session.add(self)
        db.session.commit(self)

class DownVote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key = True)
    downvote = db.Column(db.Integer,default = 0)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_downvote(self):
        db.session.add(self)
        db.session.commit()






   

    
    

