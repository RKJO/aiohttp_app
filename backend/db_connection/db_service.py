import aiopg.sa

from config.settings import (
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    DB_HOST,
    DB_PORT,
)

from sqlalchemy import (
    MetaData, Table, Column,
    Integer, String,
)

__all__ = ['user']

meta = MetaData()

user = Table(
    'user', meta,

    Column('id', Integer, primary_key=True),
    Column('user_name', String(200), nullable=False),
)


class RecordNotFound(Exception):
    """Requested record in database was not found"""


async def pg_context(app):
    engine = await aiopg.sa.create_engine(
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()


async def get_user(conn, user_id):
    result = await conn.execute(
        user.select()
        .where(user.c.id == user_id))
    user_record = await result.first()
    if not user_record:
        msg = "User with id: {} does not exists"
        raise RecordNotFound(msg.format(user_id))

    return user_record


async def create_user(conn, user_name):
    created_user = user.insert().values(user_name=user_name)
    await conn.execute(created_user)
