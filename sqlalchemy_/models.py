import traceback
from time import sleep

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin

# url = f'mysql://{user_name}:{password}@{host}:{port}/{schema_name}'
# engine = create_engine('mysql://root:123@mysql_server:3306/testedb', echo=False)
# engine = create_engine('mysql+mysqlconnector://root:123@mysql_server:3306/testedb', echo=False)
engine = create_engine('sqlite:///teste.db', echo=False)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)


class User(Base, SerializerMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return str(self.to_dict())


def create_database():
    for _ in range(10):
        sleep(10)
        try:
            Base.metadata.drop_all(bind=engine)
            Base.metadata.create_all(bind=engine)
            break
        except:
            traceback.print_exc()
            sleep(2)


if __name__ == '__main__':
    create_database()
