from datetime import datetime
from database import get_db
from database.models import User, PostImg
from database.security import create_access_token


def get_all_user_db():
    db = next(get_db())
    all_user = db.query(User).all()
    return all_user


def register_user_db(username, lname, tellNo, password, city, ):
    db = next(get_db())
    checker = db.query(User).filter_by(tellNo=tellNo).first()
    if checker:
        return 'This number is already used'
    else:
        new_user = User(username=username, lname=lname, tellNo=tellNo, password=password, city=city)
        db.add(new_user)
        db.commit()
        return 'Action done!'


def get_exact_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        return user
    else:
        return 'This user not exist!'


def log_in_db(username, password):
    db = next(get_db())
    login = db.query(User).filter_by(username=username, password=password).first()
    if login:
        token_data = {"user_id": login.user_id}
        access_token_data = create_access_token(token_data)
        return {"Access token": access_token_data, "token_type": "Bearer", "status": "Success"}
    else:
        return 'Access denied!'


def delete_user_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(user_id=user_id).first()
    if checker:
        db.delete(checker)
        db.commit()
        return 'User deleted'
    else:
        return 'This user not exist!'


def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        if edit_info == 'username':
            exact_user.username = new_info
        elif edit_info == 'lname':
            exact_user.lname = new_info
        elif edit_info != exact_user:
            return 'This argument not exist'
        db.commit()
        return 'Data successfully changed!'
    else:
        return 'User not found!'


def upload_profile_img_db(user_id, img_path):
    db = next(get_db())
    exact_user = get_exact_user_db(user_id=user_id)
    if exact_user:
        exact_user.profile_img = img_path
        db.commit()
        return 'Action done'
    else:
        return 'User not found'


def delete_profile_img_db(user_id):
    db = next(get_db())
    exact_user = get_exact_user_db(user_id)
    if exact_user:
        exact_user.profile_img = 'None'
        db.commit()
        return 'Profile photo deleted'
    else:
        return 'User not found'



























