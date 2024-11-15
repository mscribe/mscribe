from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy.sql import func


database = SQLAlchemy()


class Translation(database.Model):
    __tablename__ = "translation"

    id = Column(Integer, primary_key=True)
    language_code = Column(String(3), nullable=False)
    key = Column(String(120), nullable=False)
    value = Column(String(8000), nullable=False)
    created_date = Column(DateTime(), default=func.now())
    updated_date = Column(DateTime(), default=func.now(), onupdate=func.now())


class Blog(database.Model):
    __tablename__ = "Blog"
    id = Column(Integer, primary_key=True)
    key = Column(Integer, nullable=False, unique=True)
    title_translation_key = Column(String(120), nullable=False, unique=True)
    body_translation_key = Column(String(120), nullable=False, unique=True)
    created_date = Column(DateTime(), default=func.now())
    updated_date = Column(DateTime(), default=func.now(), onupdate=func.now())
