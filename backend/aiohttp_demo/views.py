from aiohttp import web
import json

from db_connection import db_service


async def get_user(request):
    async with request.app['db'].acquire() as conn:
        user_id = request.match_info['user_id']
        try:
            user = await db_service.get_user(conn, user_id)
        except db_service.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))
        results = {key: value for key, value in user.items()}
        return web.Response(body=json.dumps(results), status=200)


async def create_user(request):
    async with request.app['db'].acquire() as conn:
        user_name = request.query['user_name']
        try:
            new_user = await db_service.create_user(conn, user_name)

        except (KeyError, TypeError, ValueError) as e:
            raise web.HTTPBadRequest(
                text='You have not specified proper value') from e
        result = [dict(row) for row in new_user]
        return web.Response(text=json.dumps(result[0]), status=200)
