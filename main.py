from typing import Optional, List, Union

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
import sentry_sdk

sentry_sdk.init(
    dsn="https://1373feb551490e49d6ec8580c5fd7423@o1110400.ingest.sentry.io/4506525927276544",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = FastAPI(
    title="FastAPI MLS",
    description="FastAPI MLS",
    version="0.1.0",
    openapi_url="/openapi.json",
    contact={
        "name": "Elias",
        "email": "earayad@hotmail.cl",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

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

@app.get("/users", response_model=list[User])
def get_users():
    return users

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/{id}")
def get_user(
    id: int = Path(..., description="The ID of the user to get", gt=2), 
    q: str = Query(None, max_length=5)):
    if id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "user": users[id],
        "query": q
    }
        


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0