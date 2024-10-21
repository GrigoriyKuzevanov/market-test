from contextlib import asynccontextmanager

import uvicorn
from api import router as api_router
from core.config import settings
from core.models import db_connector
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on start
    yield
    # on shutdown
    await db_connector.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix=settings.api_prefix.prefix)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.app_run.host,
        port=settings.app_run.port,
        reload=True,
    )
