from typing import List

from fastapi import APIRouter, Path, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.user import UserCreate, User
from api.utils.users import get_user, get_users, get_user_by_email, create_user

router = APIRouter()

@router.get("/users", response_model=List[User], status_code=200)
async def read_users(skip: int = 0, limit: int=100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users
 
@router.post("/users", response_model=User, status_code=201)
async def generate_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db=db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email with this user is already existed")
    
    return create_user(db=db, user=user)


# Path parameter:
@router.get("/user/{id}", response_model=User)
async def read_a_user( id: int, db: Session = Depends(get_db)):
    user =  get_user(db=db, user_id=id)    

    if user is None:
        raise HTTPException(status_code=404, detail="User not found!")

    return user
