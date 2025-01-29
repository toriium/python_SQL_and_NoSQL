from time import sleep

from connection import writing_engine
from base import Base


def recreate_tables():
    for _ in range(10):
        try:
            Base.metadata.drop_all(bind=writing_engine)
            Base.metadata.create_all(bind=writing_engine)
            break
        except Exception as error:
            print(error)
            sleep(2)


if __name__ == '__main__':
    recreate_tables()
