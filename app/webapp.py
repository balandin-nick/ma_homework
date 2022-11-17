from fastapi import FastAPI
from .api.routers import user_router


webapp = FastAPI()
webapp.include_router(user_router)
