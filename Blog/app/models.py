from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime 


class Quote:
  '''
  Quote class to define quote objects
  '''






class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    hash_pass = db.Column(db.String(255)) 
    

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))   

class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    description = db.Column(db.String(255))
    comment = db.relationship('Comment',backref = 'blog',lazy='dynamic')


    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def clear_blogs(cls):
        Blog.search_blogs.clear()
    @classmethod
    def get_bloge(cls,blog_id):
        bloge=Blog.query.filter_by(user_id=id).all()
        return bloge
    @classmethod 
    def get_blogs(cls):
        blogs = Blog.query.filter_by().all()
        return Blogs
    


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String())
    blog_id = db.Column(db.Integer,db.ForeignKey("blog.id"))
    content = db.Column(db.String(255))



    @classmethod
    def sace_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()

    @classmethod
    def get_blogz(cls):
        blogz=Blog.query.filter_by().all()
        return blogz

    @classmethod 
    def get_bloge(cls):
        bloge = Blog.query.filter_by().all()
        return bloge 
    


class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    




