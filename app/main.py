from fastapi import FastAPI
from typing import List
from models import User, Gender ,Role
from uuid import uuid4 , UUID

app = FastAPI()

db: List[User] = [
    User(
    id=UUID('ff30ed3a-62ff-49e2-b400-ff06ce0adfe5'),
    first_name='Joe',
    last_name='Riko',
    middle_name="Dyu",
    gender=Gender.male,
    roles=[Role.student]
    ), 
    User(
    id=UUID('9f813122-7a6b-46de-99d8-c2407e51d3bd'),
    first_name='Alex',
    last_name='Hio',
    middle_name="Miya",
    gender=Gender.female,
    roles=[Role.admin]
    )
]

@app.get('/api/v1/users')
async def fetch_users():
    return db;

@app.post('/api/v1/users')
async def register_user(user:User):
    db.append(user)
    return {'id': user.id}