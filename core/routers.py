from fastapi import APIRouter, Depends
from posting.api.v1 import router as posting_router

router = APIRouter()

router.include_router(posting_router)


@router.get('/')
def start():
    return {"message": "Welcome!."}
