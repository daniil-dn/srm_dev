from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_login():
    return "login app created!"
