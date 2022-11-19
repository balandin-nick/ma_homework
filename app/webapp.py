from fastapi import FastAPI

from app.api.routers import user_router


app = FastAPI()
app.include_router(user_router)
