from collections import OrderedDict
from contextlib import contextmanager
from datetime import datetime

import psycopg2
from psycopg2.extras import RealDictCursor
from src.settings import DatabaseEnv
from psycopg2.extensions import connection as pg_connection
from pypika import Query, Table, Field, Schema


@contextmanager
def get_connection() -> pg_connection:
    connection = psycopg2.connect(
        database=DatabaseEnv.DB_NAME,
        user=DatabaseEnv.DB_USER,
        password=DatabaseEnv.DB_PASSWORD,
        host=DatabaseEnv.DB_HOST,
        port=DatabaseEnv.DB_PORT
    )

    try:
        yield connection
    finally:
        connection.close()


@contextmanager
def get_cursor(connection: pg_connection) -> RealDictCursor:
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    try:
        yield cursor
    finally:
        cursor.close()


class DBUtils:
    @staticmethod
    def execute(query: str, params: list = None) -> None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, params)
                connection.commit()

    @staticmethod
    def executemany(query: str, params: list[list] = None) -> None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.executemany(query, params)
                connection.commit()

    @staticmethod
    def query_all(query: str, params: list = None) -> list[dict]:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result if result else []

    @staticmethod
    def query_one(query: str, params: list = None) -> dict | None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, params)
                result = cursor.fetchone()
                return result if result else None

    @staticmethod
    def create_insert_stm(schema, table: str, params: OrderedDict[str, any]) -> str:
        schema = Schema(schema)
        table = Table(table, schema=schema)

        stm = Query.into(table)
        stm = stm.columns(list(params.keys()))
        stm = stm.insert(list(params.values()))

        return stm.get_sql()

    @staticmethod
    def create_multiple_insert_stm(schema, table: str, params: list[OrderedDict[str, any]]) -> str:
        schema = Schema(schema)
        table = Table(table, schema=schema)

        stm = Query.into(table)
        stm = stm.columns(list(params[0].keys()))
        for param in params:
            stm = stm.insert(list(param.values()))

        return stm.get_sql()

    @staticmethod
    def create_update_stm(schema, table: str, params: dict[str, any], where_expressions: list | None = None) -> str:
        schema = Schema(schema)
        table = Table(table, schema=schema)

        stm = Query.update(table)
        for column, value in params.items():
            stm = stm.set(Field(column), value)

        if where_expressions:
            for where_expression in where_expressions:
                stm = stm.where(where_expression)

        return stm.get_sql()


if __name__ == '__main__':
    ...
    # query = """
    # SELECT "key", value
    # FROM gl_data.key_value
    # WHERE key = 'voluum_api'
    # """
    # r = DBUtils.query_one(query)
    # r2 = DBUtils.query_all(query)
    # print(r)

    # --------------------------- Update ---------------------------
    # params = {
    #     "field1": 1,
    #     "field2": "2",
    # }
    # stm = DBUtils.create_update_stm(schema='gl_data', table='customer_io', params=params,
    #                                 where_expressions=[Field('id') == 5])
    # print(stm)

    # --------------------------- Insert ---------------------------
    # params = OrderedDict(
    #     cio_id='user-1234',
    #     email='5555@gmail.com',
    #     delivery_id='RAECAAFwnUSneIa0ZXkmq8EdkAM==',
    #     event_id='01E2EMRMM6TZ12TF9WGZN0WJQT',
    #     metric='clicked',
    #     object_type='email',
    #     sent_date=None,
    #     clicked_date=datetime(2024, 4, 18, 20, 33, 18),
    #     converted_date=None,
    # )
    # stm = DBUtils.create_insert_stm(schema='gl_data', table='customer_io', params=params)
    # DBUtils.execute(stm)
    # print(stm)
