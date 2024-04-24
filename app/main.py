from fastapi import FastAPI
from repository import UserRepository
from models import User, UserUpdateRequest
from uuid import UUID

app = FastAPI()
user_repository = UserRepository()

@app.get('/api/v1/users')
async def fetch_users():
    return user_repository.get_all()

@app.post('/api/v1/users')
async def register_user(user: User):
    return user_repository.add(user)

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    return user_repository.delete(user_id)

@app.put("/api/v1/users/{user_id}")
async def change_user(user_update: UserUpdateRequest, user_id: UUID):
    return user_repository.update(user_update, user_id)