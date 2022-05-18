from aiohttp import web
from .views import (
    get_user,
    create_user
)


def setup_routes(app):
    app.add_routes([
        web.get(r'/get_user/{user_id:\d+}', get_user),
        web.post('/create_user', create_user)
    ])
