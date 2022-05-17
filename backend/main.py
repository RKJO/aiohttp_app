from aiohttp import web

from db_connection.db_service import pg_context
from aiohttp_demo.routes import setup_routes


async def init_app():

    app = web.Application()

    # create db connection on startup, shutdown on exit
    app.cleanup_ctx.append(pg_context)

    # setup views and routes
    setup_routes(app)

    return app


def main():
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
