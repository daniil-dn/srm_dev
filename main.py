import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.routers import router
from core.config import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
app.include_router(router)
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8081, loop="asyncio")
