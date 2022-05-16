from aiohttp import web
import json


async def get_user(request):
    try:
        user_id = request.match_info['user_id']
        response_obj = {
            'status': 'success', 'message': f'User ID to: {user_id}'
        }

        return web.Response(
            text=json.dumps(response_obj),
            status=200
        )

    except Exception as e:
        response_obj = {
            'status': 'failed', 'message': str(e)
        }
        return web.Response(text=json.dumps(response_obj), status=500)


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