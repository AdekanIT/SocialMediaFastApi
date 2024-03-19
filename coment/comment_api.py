from fastapi import APIRouter
from coment import Comment, EditComment
from database.commentservice import add_comment_db, change_comment_db, delete_comment_db, all_comment_db


comment_router = APIRouter(prefix='/comment', tags=['Methods for comment'])


@comment_router.get('/all-comment')
async def all_comment():
    comments = all_comment_db()
    return comments


@comment_router.post('/add-comment')
async def add_comment(data: Comment):
    comment = add_comment_db(**data.model_dump())
    if comment:
        return {'message': comment}
    else:
        return {'message': 'Error with comment!'}


@comment_router.put('/edit-comment')
async def edit_comment(data: EditComment):
    edit = change_comment_db(**data.model_dump())
    if edit:
        return {'message': edit}
    else:
        return {'message': 'Comment not found!'}


@comment_router.delete('/delete-comment')
async def delete_comment(comment_id):
    delete = delete_comment_db(comment_id)
    if delete:
        return {'message': delete}
    else:
        return {'message': 'Comment not found'}