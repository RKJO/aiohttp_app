from sqlalchemy import create_engine, MetaData

from db_connection.db_service import user
from config.settings import (
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    DB_HOST,
    DB_PORT,
    DATABASE_URL
)

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

ADMIN_DB_URL = DSN.format(
    user=POSTGRES_USER, password=POSTGRES_PASSWORD, database=POSTGRES_DB,
    host=DB_HOST, port=DB_PORT
)

admin_engine = create_engine(ADMIN_DB_URL, isolation_level='AUTOCOMMIT')


# def setup_db():
#     db_name = POSTGRES_DB
#     db_user = POSTGRES_USER
#     db_pass = POSTGRES_PASSWORD
#
#     conn = admin_engine.connect()
#     # conn.execute("DROP DATABASE IF EXISTS %s" % db_name)
#     # conn.execute("DROP ROLE IF EXISTS %s" % db_user)
#     conn.execute("CREATE USER %s WITH PASSWORD '%s'" % (db_user, db_pass))
#     conn.execute("CREATE DATABASE %s ENCODING 'UTF8'" % db_name)
#     conn.execute("GRANT ALL PRIVILEGES ON DATABASE %s TO %s" %
#                  (db_name, db_user))
#     conn.close()


def create_tables(engine=admin_engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[user])


# def drop_tables(engine=admin_engine):
#     meta = MetaData()
#     meta.drop_all(bind=engine, tables=[user])


def sample_data(engine=admin_engine):
    conn = engine.connect()
    conn.execute(user.insert(), [
        {'user_name': "Roman"}
    ])
    # user.insert().values(user_name="Roman")
    conn.close()


if __name__ == '__main__':
    # setup_db()
    create_tables()
    sample_data()
