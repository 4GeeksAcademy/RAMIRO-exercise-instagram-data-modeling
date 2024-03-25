import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

user_follower = Table('User-Follower',
             Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('follower_id', Integer, ForeignKey('user.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name= Column(String(250), nullable=False)
    last_name= Column(String(250), nullable=False)
    email= Column(String(250), nullable=False)
    followers = relationship('Follower', secondary=user_follower, lazy='subquery',
        backref=backref('pages', lazy=True))
    user_one_to_many = relationship('User', backref='comment', lazy=True)
    user_one_to_many1 = relationship('User', backref='post', lazy=True)


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_text= Column(String(250), nullable=False)

    
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_one_to_many = relationship('Post', backref='comment', lazy=True)
    post_one_to_many1 = relationship('Post', backref='media', lazy=True)
    
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(Integer, primary_key=True)
    url =  Column(String(250), nullable=False)
    post_id= Column(Integer, ForeignKey('post.id'))
    
class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer, primary_key=True)
    # user_from_id = Column(Integer, ForeignKey('user.id'))
    # user_to_id = Column(Integer, ForeignKey('user.id'))
    # Media = relationship(Media)
    # url = Column(String(250), ForeignKey('media.id'))
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
