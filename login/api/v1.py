from fastapi import APIRouter, Body

from auth.auth_handler import signJWT
from login.models import UserLogin, User

router = APIRouter()

users = []


def check_user(user_data: UserLogin):
    for user in users:
        if user.email == user_data.email and user.password == user_data.password:
            return True
    return False


@router.post("/signup")
async def signup_user(user: User = Body(...)):
    users.append(user)  # Todo Make db call, making sure to hash the password first
    return signJWT(user.email)


@router.post("/login")
async def login_user(user: UserLogin = Body(...)):
    users.append(user)
    return signJWT(user.email)
