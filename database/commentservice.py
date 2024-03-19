from database.models import Comment
from database import get_db
from datetime import datetime


def add_comment_db(post_id, comment_text, user_id):
    db = next(get_db())
    new_comment = Comment(post_id=post_id, comment_text=comment_text, user_id=user_id, pub_date=datetime.now())
    if new_comment:
        db.add(new_comment)
        db.commit()
        return new_comment
    else:
        return 'Action fail'


def delete_comment_db(post_id, comment_id):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(post_id=post_id, comment_id=comment_id).first()
    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return 'Comment deleted'
    else:
        return 'Comment not found'


def change_comment_db(post_id, comment_id, new_text):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(post_id=post_id, comment_id=comment_id).first()
    if exact_comment:
        exact_comment.comment_text = new_text
        db.commit()
        return 'Comment changed'
    else:
        return 'Comment not found'
































