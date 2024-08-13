from typing import List

from fastapi import APIRouter, Path, Query
from pydantic import BaseModel

router = APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: str | None = None  # this is an optional field

class GetUser(BaseModel):
    message: str
    user: User | None = None
    query: str | None = None

@router.get("/users", response_model=List[User])
# @router.get("/users")
async def get_users():
    # return {"user": users}
    return users
 
@router.post("/users")
async def create_user(user: User):
    users.append(user)
    # return {"msg": f"user {user} is created"}
    return "success"

# # Path parameter:
@router.get("/user/{id}", response_model=GetUser)
async def get_user(id: int):
    try:
        user_id = int(id) - 1
        print(user_id)
        user = users[user_id]
        # return f"{user} with parameter {q}"
        return {"message": "success", "user":user }
    except:
        return {"message": "Not found"}

    
# Query parameter:
@router.get("/special-user/{id}", response_model=GetUser | str)
async def get_special_user(
    id: int = Path(..., description="User's Id", gt=0), 
    q: str = Query(None, max_length=5)
    ):
    try:
        user_id = int(id) -1
        user = users[user_id]
        # return f"{user} with parameter: {q}"
        return {"message": "success", "user":user, "query": q }
    except:
        return 'not found'
    
