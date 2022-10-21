from fastapi import APIRouter, Depends
from auth.auth_bearer import JWTBearer

from ..models import PostSchema

posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    }
]

router = APIRouter()


@router.get("/posts", tags=["posts"], dependencies=[Depends(JWTBearer())])
async def get_posts() -> dict:
    return {"data": posts}


@router.get("/posts/{id}", tags=["posts"], dependencies=[Depends(JWTBearer())])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@router.post("/posts", tags=["posts"], dependencies=[Depends(JWTBearer())])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }
