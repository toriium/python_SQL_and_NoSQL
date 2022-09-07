from typing import Union, List

from contextlib import contextmanager
import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import CursorBase


@contextmanager
def get_connection() -> MySQLConnection:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        port=3306,
        db='starwars',
    )

    try:
        yield conexao
    finally:
        conexao.close()


@contextmanager
def get_cursor(connection: MySQLConnection) -> CursorBase:
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
    finally:
        cursor.close()


class DataBase:
    @staticmethod
    def execute(query: str, arguments: List = None) -> None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, arguments)
                connection.commit()

    @staticmethod
    def executemany(query: str, arguments: List[List] = None) -> None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.executemany(query, arguments)
                connection.commit()

    @staticmethod
    def consult_all(query: str, arguments: List = None) -> Union[List[dict], None]:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, arguments)
                result = cursor.fetchall()
                return result if result else None

    @staticmethod
    def consult_one(query: str, arguments: List = None) -> Union[dict, None]:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, arguments)
                result = cursor.fetchone()
                return result if result else None


if __name__ == '__main__':
    ...
