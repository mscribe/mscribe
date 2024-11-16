from enum import Enum as PyEnum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


database = SQLAlchemy()


class Translation(database.Model):
    __tablename__ = "translation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    language_code = Column(String(3), nullable=False)
    key = Column(String(120), nullable=False)
    value = Column(String(8000), nullable=False)
    created_date = Column(DateTime(), default=func.now())
    updated_date = Column(DateTime(), default=func.now(), onupdate=func.now())


class Tag(database.Model):
    __tablename__ = "Tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
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

    class BlogStatus(PyEnum):
        DRAFT = "DRAFT"
        PUBLISHED = "PUBLISHED"
        ARCHIVED = "ARCHIVED"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(Integer, nullable=False, unique=True)
    tk_title = Column(String(120), nullable=False, unique=True)
    tk_body = Column(String(120), nullable=False, unique=True)
    image_url = Column(String(255), nullable=True)
    tk_difficulty = Column(String(120), nullable=False)
    reading_time = Column(Integer, nullable=False)
    readers_count = Column(Integer, default=0, nullable=False)
    status = Column(Enum(BlogStatus), nullable=False)
    created_date = Column(DateTime(), default=func.now())
    updated_date = Column(DateTime(), default=func.now(), onupdate=func.now())

    blog_readers = relationship("BlogReader", back_populates="blog")


class BlogReader(database.Model):
    __tablename__ = "BlogReader"

    id = Column(Integer, primary_key=True, autoincrement=True)
    reader_ip = Column(String(40), nullable=False)
    blog_id = Column(Integer, ForeignKey('Blog.id'), nullable=False)
    read_date = Column(DateTime(), default=func.now())

    blog = relationship("Blog", back_populates="blog_readers")
