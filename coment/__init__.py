from pydantic import BaseModel


class Comment(BaseModel):
    post_id: int
    user_id: int
    comment_text: str


class EditComment(BaseModel):
    post_id: int
    comment_id: int
    new_text: str
