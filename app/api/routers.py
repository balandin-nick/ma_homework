from fastapi_crudrouter import SQLAlchemyCRUDRouter

from app.api.models import UserModel, UserSchema
from app.db import UserDBModel
from app.db.base import get_session


user_router = SQLAlchemyCRUDRouter(
    schema=UserSchema,
    create_schema=UserModel,
    db_model=UserDBModel,
    db=get_session,
    prefix='user'
)
