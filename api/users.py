from typing import Optional, List, Union
from fastapi import FastAPI, HTTPException, Path, Query, APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    name: str
    age: Optional[int]
    email: str
    phone: Union[str, None] = None
    
users = [
  User(name="Camilo", age=21, email=" ", phone=""),
  User(name="Andres", age=21, email=" ", phone=""),
  User(name="David", age=21, email=" ", phone=""),
  User(name="Juan", age=21, email=" ", phone=""),
]

@router.get("/users", response_model=list[User])
def get_users():
    return users

@router.post("/users")
def create_user(user: User):
    users.append(user)
    return user

@router.get("/users/{id}")
def get_user(
    id: int = Path(..., description="The ID of the user to get", gt=2), 
    q: str = Query(None, max_length=5)):
    if id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "user": users[id],
        "query": q
    }