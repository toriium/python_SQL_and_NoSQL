import traceback
from time import sleep

from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from connection import writing_engine

from base import Base


class User(Base, SerializerMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return str(self.to_dict())


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
