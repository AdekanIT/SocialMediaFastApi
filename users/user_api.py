from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from users import LogIn, SingUp, EditUser
from database.userservice import (register_user_db, log_in_db, get_all_user_db, get_exact_user_db, delete_user_db,
                                  edit_user_info_db, upload_profile_img_db, delete_profile_img_db)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
user_router = APIRouter(prefix='/user', tags=['Methods for users'])


@user_router.post('/register')
async def user_regist(data: SingUp):
    result = register_user_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'User already exist!'}


@user_router.post('/login')
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = log_in_db(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect tell number or password')
    else:
        return user


@user_router.get('/users')
async def all_users():
    return get_all_user_db()


@user_router.get('/user')
async def exact_user(user_id):
    user = get_exact_user_db(user_id)
    return user


@user_router.delete('/delete-user')
async def delete_user(user_id):
    user = delete_user_db(user_id)
    return user


@user_router.put('/edit-user')
async def edit_user(data: EditUser):
    edit = edit_user_info_db(**data.model_dump())
    return edit


@user_router.put('user-img')
async def upload_user_img(user_id, img_path):
    img = upload_profile_img_db(user_id, img_path)
    return img


@user_router.delete('/delete-img')
async def delete_user_img(user_id):
    img = delete_profile_img_db(user_id)
    return img













































































































