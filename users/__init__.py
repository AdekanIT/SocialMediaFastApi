from pydantic import BaseModel


class SingUp(BaseModel):
    username: str
    lname: str
    tellNo: str
    password: str
    city: str


class LogIn(BaseModel):
    tellNo: str
    password: str


class EditUser(BaseModel):
    user_id: int
    edit_info: str
    new_info: str