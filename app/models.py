from . import db


class users(db.Model):
    id                  = db.Column(db.Integer, primary_key=True)
    username            = db.Column(db.String(80), unique=True)
    password            = db.Column(db.String(80), unique=True)
    first_name          = db.Column(db.String(80))
    last_name           = db.Column(db.String(80))
    email               = db.Column(db.String(80), unique=True)
    location            = db.Column(db.String(80))
    biography           = db.Column(db.String(225))
    profile_photo_url   = db.Column(db.String(80))
    joined_on           = db.Column(db.String(80))    

    followers = db.relationship('follows', backref='users', lazy=True)
    userposts = db.relationship('posts', backref='users', lazy=True)

    def __init__(self, username, email,first_name,last_name,password,location,biography,profile_photo_url,joined_on):
        self.username           = username
        self.password           = password
        self.first_name         = first_name
        self.last_name          = last_name
        self.email              = email
        self.location           = location
        self.biography          = biography
        self.profile_photo_url  = profile_photo_url
        self.joined_on          = joined_on


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
        
class likes(db.Model):
    id       = db.Column(db.Integer, primary_key=True) 
    user_id  = db.Column(db.Integer, db.ForeignKey('users.id'))  
    post_id  = db.Column(db.Integer, db.ForeignKey('posts.id'))  
    

class follows (db.Model):
    id          = db.Column(db.Integer, primary_key=True)           
    user_id     = db.Column(db.Integer,db.ForeignKey('users.id'))           
    follower_id = db.Column(db.Integer,db.ForeignKey('follows.id'))                
        
        
class posts (db.Model):
    id         = db.Column(db.Integer, primary_key=True)    
    user_id    = db.Column(db.Integer,db.ForeignKey('users.id'))          
    photo      = db.Column(db.String)        
    caption    = db.Column(db.String)       
    created_on = db.Column(db.String)
    
    postlikes = db.relationship('likes', backref='posts', lazy=True)
