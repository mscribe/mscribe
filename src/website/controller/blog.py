from __future__ import annotations
from datetime import datetime

from typing import List
from typing import Tuple

from website.data import BlogData
from website.schema import Blog
from website.objects.models import KeyValue
from website.objects.models import BlogModel
from website.controller.translation import TranslationController as tc

from flask_sqlalchemy.pagination import Pagination


class BlogController:
    @staticmethod
    def get_blog(language: str, blog_key: str) -> BlogModel:
        blog = BlogData.get_blog(blog_key)

        title = tc.get_translation(language, blog.tk_title)
        body = tc.get_translation(language, blog.tk_body)
        status = tc.get_translation(language, blog.tk_status.value)

        value = tc.get_translation(language, blog.tk_difficulty.value)
        difficulty = KeyValue(key=blog.tk_difficulty.name, value=value)

        created_date = datetime.strftime(blog.created_date, "%-d %b %Y")
        updated_date = datetime.strftime(blog.updated_date, "%-d %b %Y")

        return BlogModel(key=blog.key,
                         title=title,
                         body=body,
                         image_url=blog.image_url,
                         difficulty=difficulty,
                         reading_time=blog.reading_time,
                         readers=blog.readers,
                         status=status,
                         created_date=created_date,
                         updated_date=updated_date)

    @staticmethod
    def get_blogs(language: str,
                  page=1,
                  per_page=20,
                  is_desc: bool = True) -> Tuple[List[BlogModel], Pagination]:

        blogs = []
        pagination = BlogData.get_blogs(page, per_page, is_desc)
        blogs_items: List[Blog] = pagination.items

        for blog in blogs_items:
            title = tc.get_translation(language, blog.tk_title)
            body = tc.get_translation(language, blog.tk_body)
            status = tc.get_translation(language, blog.tk_status.value)

            value = tc.get_translation(language, blog.tk_difficulty.value)
            difficulty = KeyValue(key=blog.tk_difficulty.name, value=value)

            created_date = datetime.strftime(blog.created_date, "%-d %b %Y")
            updated_date = datetime.strftime(blog.updated_date, "%-d %b %Y")

            blogs.append(
                BlogModel(key=blog.key,
                          title=title,
                          body=body,
                          image_url=blog.image_url,
                          difficulty=difficulty,
                          reading_time=blog.reading_time,
                          readers=blog.readers,
                          status=status,
                          created_date=created_date,
                          updated_date=updated_date))

        return blogs, pagination
