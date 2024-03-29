from typing import List

from pydantic import BaseModel


class ToDoSchema(BaseModel):
    id: int
    contents: str
    is_done: bool

    class Config:
        from_attributes = True


class ToDoListSchema(BaseModel):
    todos: List[ToDoSchema]


class UserSchema(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class JWTResponse(BaseModel):
    access_token: str
