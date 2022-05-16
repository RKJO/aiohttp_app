from aiohttp import web
from .views import (
    get_user,
    # create_user
)


def setup_routes(app):
    # app.router.add_get('/get_user', get_user, name='get_user')
    # app.router.add_post('/create_user', create_user, name='create_user')
    app.add_routes([
        web.get(r'/get_user/{user_id:\d+}', get_user),
        # web.post('/create_user', create_user)
    ])
