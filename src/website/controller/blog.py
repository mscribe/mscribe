from __future__ import annotations

from typing import List
from typing import Tuple

from website.data import BlogData
from website.controller import TranslationController
from website.objects.models import BlogModel

from flask_sqlalchemy.pagination import Pagination

 
class BlogController:
    @staticmethod
    def get_blogs(language: str,
                  page=1,
                  per_page=20,
                  is_desc: bool = True) -> Tuple[Pagination, List[BlogModel]]:

        blogs = []

        pagination = BlogData.get_blogs(page, per_page, is_desc)

        for blog in pagination.items:
            blogs.append(
                BlogModel(title=blog.title,
                          )
            )
