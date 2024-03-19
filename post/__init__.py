from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    user_id: int
    post_text: str


class EditPost(BaseModel):
    post_id: int
    new_text: str


class PostImg(BaseModel):
    post_id: int
    img_path: str