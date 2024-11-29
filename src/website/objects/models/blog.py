from dataclasses import dataclass
from datetime import datetime

from website.objects.enums import BlogStatusEnum


@dataclass
class BlogModel:
    key: str
    title: str
    body: str
    image_url: str
    difficulty: str
    reading_time: int
    readers: int
    status: BlogStatusEnum
    created_date: datetime
    updated_date: datetime
