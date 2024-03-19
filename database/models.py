from database import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Date, ForeignKey, Text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String)
    lname = Column(String)
    tellNo = Column(String, unique=True)
    password = Column(String)
    city = Column(String)
    birthday = Column(Date)
    profile_img = Column(String)


class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(ForeignKey('user.user_id'))
    post_text = Column(Text)
    like = Column(Integer, default=0)
    pub_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


class PostImg(Base):
    __tablename__ = 'post_img'
    img_id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(ForeignKey('post.post_id'))
    img_path = Column(String)

    post_fk = relationship(Post, lazy='subquery')


class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(ForeignKey('post.post_id'))
    user_id = Column(ForeignKey('user.user_id'))
    comment_text = Column(Text)
    pub_date = Column(DateTime)

    post_fk = relationship(Post, lazy='subquery')
    user_pk = relationship(User, lazy='subquery')