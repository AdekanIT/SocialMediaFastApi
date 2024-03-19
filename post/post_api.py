from fastapi import APIRouter, Depends, HTTPException, UploadFile, Body
from database.postservice import (get_all_post_db, delete_img_post_db, get_exact_post_db, upload_img_post_db,
                                  edit_post_text_db, add_new_post_db, add_like_post_db, unlike_post_db, delete_post_db)
from post import Post, EditPost

post_router = APIRouter(prefix='/posts', tags=['Methods for post'])


@post_router.post('/public_post')
async def public_post(data: Post):
    result = add_new_post_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}


@post_router.get('all_post')
async def all_posts():
    posts = get_all_post_db()
    return posts


@post_router.post('/add-photo')
async def add_photo(post_id, img_path: UploadFile = None):
    with open(f'media/{img_path.filename}', 'wb') as file:
        user_photo = await img_path.read()
        file.write(user_photo)

    result = upload_img_post_db(post_id, f'/media/{img_path.file}')

    if result:
        if result:
            return {'message': result}
        else:
            return {'message': 'Error with upload!'}


@post_router.get('/get_posst')
async def get_post(post_id: int):
    result = get_exact_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}


@post_router.post('/like')
async def add_like(post_id: int):
    like = add_like_post_db(post_id)
    if like:
        return {'message': like}
    else:
        return {'message': 'Post not found'}


@post_router.post('/unlike')
async def unlike(post_id: int):
    like = unlike_post_db(post_id)
    if like:
        return {'message': like}
    else:
        return {'message': 'Post not found'}


@post_router.delete('/delete-post-img')
async def delete_post_img(post_id: int):
    delete = delete_img_post_db(post_id)
    if delete:
        return {'message': delete}
    else:
        return {'message': 'Post not found'}


@post_router.delete('/delete_post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}


@post_router.put('/edit-post')
async def edit_post(data: EditPost):
    result = edit_post_text_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}









































