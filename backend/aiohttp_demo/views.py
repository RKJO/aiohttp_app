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


# async def create_user(request):
#     try:
#         user_id = request.match_info['user_id']
#
#         return web.Response(
#             text=f'user id {user_id}',
#             status=200
#         )
#
#     except Exception as e:
#         response_obj = {
#             'status': 'failed', 'message': str(e)
#         }
#         return web.Response(text=json.dumps(response_obj), status=200)