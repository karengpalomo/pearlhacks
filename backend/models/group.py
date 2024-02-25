from pydantic import BaseModel


class Group(BaseModel):
    id: int | None = None
    name: str = ''
    members: ['User'] = [] 
