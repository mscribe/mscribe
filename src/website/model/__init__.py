from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
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


class Tag(database.Model):
    __tablename__ = "Tag"
    id = Column(Integer, primary_key=True)
    tk_name = Column(String(100), nullable=False, unique=True)
    created_date = Column(DateTime(), default=func.now())
    updated_date = Column(DateTime(), default=func.now(), onupdate=func.now())


class BlogTag(database.Model):
    __tablename__ = "blogtag"
    blog_id = Column(Integer, ForeignKey("Blog.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("Tag.id"), primary_key=True)
    created_date = Column(DateTime(), default=func.now())


class Blog(database.Model):
    __tablename__ = "Blog"
    id = Column(Integer, primary_key=True)
    key = Column(Integer, nullable=False, unique=True)
    tk_title = Column(String(120), nullable=False, unique=True)
    tk_body = Column(String(120), nullable=False, unique=True)
    tk_difficulty = Column(String(120), nullable=False, unique=True)
    reading_time = Column(Integer, nullable=False)
    image_url = Column(String(255), nullable=True)
    created_date = Column(DateTime(), default=func.now())
    updated_date = Column(DateTime(), default=func.now(), onupdate=func.now())
