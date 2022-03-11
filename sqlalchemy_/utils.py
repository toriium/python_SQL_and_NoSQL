from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from models import engine, User


@contextmanager
def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()


def select_obj(obj, kw_filters):
    with create_session() as session:
        resultado = session.query(obj).filter_by(**kw_filters).first()
        session.close()
        return resultado


def insert_obj(obj):
    with create_session() as session:
        session.add(obj)
        session.flush()
        session.commit()


def update_obj_by_id(obj, obj_id, obj_update):
    with create_session() as session:
        session.query(obj).filter_by(id=obj_id).update(obj_update)
        session.flush()
        session.commit()
        session.close()


def delete_obj_by_id(obj, obj_id):
    with create_session() as session:
        session.query(obj).filter_by(id=obj_id).delete()
        session.flush()
        session.commit()


if __name__ == '__main__':
    ...
    # with create_session() as session:
    #     config = {'age': '10'}
    #     print(config)
    #     results = session.query(User).filter_by(**config).all()
    #     for row in results:
    #         print(row.name)

    # ------------------------------------- use of create_session -------------------------------------
    # Form - 1
    # with create_session() as session:
    #     var = session.query(User).filter_by(id=2).first()
    #     print(var.name)

    # Form - 2
    with create_session() as session:
        results = session.query(User).all()
        for row in results:
            print(row.name)

    # ------------------------------------- use of select_obj_by_id -------------------------------------
    # var = select_obj_by_id(obj=User, obj_id=2)
    # print(var)

    # ------------------------------------- use of update_obj_by_id -------------------------------------
    # Form - 1
    # update_obj_by_id(obj=User, obj_id=2, obj_update={User.name: 'zabuza', User.age: 50})

    # Form - 2
    # update_dict = {}
    # update_dict[User.name] = 'aristoteles'
    # update_dict[User.age] = 48
    # update_obj_by_id(obj=User, obj_id=2, obj_update=update_dict)

    # ------------------------------------- use of insert_obj -------------------------------------
    # Form - 1
    obj_user = User(name='nietzsche', age=55)
    insert_obj(obj=obj_user)

    # Form - 2
    # obj_user = User()
    # obj_user.name = 'platao'
    # obj_user.age = 65
    # insert_obj(obj=obj_user)

    # ------------------------------------- use of delete_obj_by_id -------------------------------------
    # delete_obj_by_id(obj=User, obj_id=2)
