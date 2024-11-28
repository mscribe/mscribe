from website.schema import Blog

from flask_sqlalchemy import pagination


class BlogController:
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
