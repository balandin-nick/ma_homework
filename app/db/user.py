from sqlalchemy import Column, Integer, String

from app.db.base import BaseDBMetaModel


__all__ = [
    "UserModel",
]


class UserModel(BaseDBMetaModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    phone = Column(String)

    def __repr__(self):
        return f"UserModel(id={self.id!r}, name={self.username!r})"
