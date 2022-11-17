from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import UserModel, UserSchema
from .models.db import UserDBModel
from .models.db.base import get_session


user_router = SQLAlchemyCRUDRouter(
    schema=UserSchema,
    create_schema=UserModel,
    db_model=UserDBModel,
    db=get_session,
    prefix='user'
)
