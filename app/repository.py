from fastapi import HTTPException
from typing import List
from models import User, Gender ,Role , UserUpdateRequest
from uuid import UUID


class UserRepository:
    def __init__(self):
        self.db: List[User] = [
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

    def get_all(self):
        return self.db

    def add(self, user: User):
        self.db.append(user)
        return {'id': user.id}

    def delete(self, user_id: UUID):
        for user in self.db:
            if user.id == user_id:
                self.db.remove(user)
                return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )

    def update(self, user_update: UserUpdateRequest, user_id: UUID):
        for user in self.db:
            if user.id == user_id:
                if user_update.first_name is not None:
                    user.first_name = user_update.first_name
                if user_update.last_name is not None:
                    user.last_name = user_update.last_name
                if user_update.middle_name is not None:
                    user.middle_name = user_update.middle_name
                if user_update.roles is not None:
                    user.roles = user_update.roles
                return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )
