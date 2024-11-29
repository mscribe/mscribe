from website.schema import Blog

from flask_sqlalchemy import pagination


class BlogData:
    @staticmethod
    def get_blog(blog_id: int) -> Blog:
        return Blog.query\
            .filter(Blog.id == blog_id)\
            .first()

    @staticmethod
    def get_blogs(page=1,
                  per_page=20,
                  is_desc: bool = True) -> pagination:

        if is_desc:
            order_by = Blog.created_date.desc()
        else:
            order_by = Blog.created_date.asc()

        query = Blog.query.order_by(order_by)

        return query.paginate(page=page,
                              per_page=per_page,
                              error_out=False)
