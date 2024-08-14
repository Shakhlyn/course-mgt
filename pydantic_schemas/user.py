from datetime import datetime

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    role: int

class UserCreate(UserBase):
    ...

# This schema should be same as defined in model: db/models/user.py
class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class config:
        orm_mode = True     # we must define this class to interact with the ORM
