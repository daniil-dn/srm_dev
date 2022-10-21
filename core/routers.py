from fastapi import APIRouter, Depends
from posting.api.v1 import router as posting_router
from login.api.v1 import router as login_router

router = APIRouter()

router.include_router(posting_router)
router.include_router(login_router)


@router.get('/')
async def start():
    return {"message": "Welcome!."}
