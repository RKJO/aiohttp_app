from aiohttp import web

# from aiohttp_demo.db import init_db
from aiohttp_demo.routes import setup_routes


async def init_app():

    app = web.Application()

    setup_routes(app)

    # db_pool = await init_db(app)

    return app


def main():
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
