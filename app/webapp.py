from fastapi import FastAPI

from app.api.routers import user_router
from app.settings.db import service_database_settings


app = FastAPI()
app.include_router(user_router)


@app.get("/")
def read_root():
    return service_database_settings.dict()
