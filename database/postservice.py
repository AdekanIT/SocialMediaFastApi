from database.models import Post, PostImg
from database import get_db
from datetime import datetime


def get_all_post_db():
    db = next(get_db())
    all_posts = db.query(Post).all()
    return all_posts


def get_exact_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(Post).filter_by(post_id=post_id).first()
    if exact_post:
        return exact_post
    else:
        return 'Post not found'


def add_new_post_db(user_id, post_text):
    db = next(get_db())
    new_post = Post(user_id=user_id, post_text=post_text, pub_date=datetime.now())
    db.add(new_post)
    db.commit()
    return new_post


def edit_post_text_db(post_id, new_text):
    db = next(get_db())
    exact_post = db.query(Post).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.post_text = new_text
        db.commit()
        return 'Text of post changed'
    else:
        return 'Post not found'


def delete_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(Post).filter_by(post_id=post_id).first()
    if exact_post:
        db.delete(exact_post)
        db.commit()
        return 'Post successfully deleted'
    else:
        return 'Post not found'


def add_like_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(Post).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.like += 1
        db.commit()
        return '+1 Like'
    else:
        return 'Post not found'


def unlike_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(Post).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.like -= 1
        db.commit()
        return '-1 Like'
    else:
        return 'Post not found'


def upload_img_post_db(post_id, img_path):
    db = next(get_db())
    new_photo = PostImg(post_id=post_id, img_path=img_path)
    if new_photo:
        db.add(new_photo)
        db.commit()
        return 'Photo added'
    else:
        return 'Action fail'


def delete_img_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(PostImg).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.img_path = None
        db.commit()
        return 'Photo deleted'
    else:
        return 'Action fail'














































