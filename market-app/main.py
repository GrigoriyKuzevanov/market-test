import uvicorn
from api import router as api_router
from core.config import settings
from fastapi import FastAPI

app = FastAPI()
app.include_router(api_router, prefix=settings.api_prefix.prefix)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.app_run.host,
        port=settings.app_run.port,
        reload=True,
    )
