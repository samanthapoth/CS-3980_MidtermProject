from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    description: str
    gender: str

class TodoRequest(BaseModel):
    title: str
    description: str
    gender: str