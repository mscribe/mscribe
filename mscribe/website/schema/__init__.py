from typing import TYPE_CHECKING

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy.sql import func


database = SQLAlchemy()


if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = database.Model


class Blog(Model):
    __tablename__ = "Blog"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(255), unique=True)
    title = Column(String(120), nullable=False, unique=True)
    body = Column(String(120), nullable=False, unique=True)
    image_url = Column(String(255), nullable=True)
    readers = Column(Integer, default=0, nullable=False)
    created_date = Column(DateTime(), default=func.now())
    updated_date = Column(DateTime(), default=func.now(), onupdate=func.now())
