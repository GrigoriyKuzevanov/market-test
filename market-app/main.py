import uvicorn
from fastapi import FastAPI

from api import api_router
from core.config import settings

app = FastAPI()
app.include_router(
    api_router,
    prefix=settings.api_prefix.prefix,
)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.run_app.host,
        port=settings.run_app.port,
        reload=settings.run_app.reload,
    )
