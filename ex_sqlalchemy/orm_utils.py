from typing import Any, Optional
from contextlib import contextmanager
from copy import copy

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from connection import SessionLocal
from errors.sql_error import SQLError


@contextmanager
def create_session() -> Session:
    """
    Way - 1
    with create_session() as session:
        var = session.query(User).filter_by(id=2).first()
        print(var.name)
    ----------------------------------------------------
    Way - 2
    with create_session() as session:
        results = session.query(User).all()
        for row in results:
            print(row.name)
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def select_first_obj(obj_table, filter_by: dict):
    """
    Way - 1
    var = select_first_obj(obj=User, filter_by={"id": 1})
    print(var)
    """
    with create_session() as session:
        query_result = session.query(obj_table).filter_by(**filter_by).first()

    return query_result if query_result else None


def select_all_obj(obj_table, filter_by: dict):
    """
    Way - 1
    vars = select_all_obj(obj=User, filter_by={"id": 1})
    for var in vars:
        print(var)
    """
    with create_session() as session:
        query_result = session.query(obj_table).filter_by(**filter_by).all()

    return query_result if query_result else None


def insert_obj(obj) -> tuple[Any, Optional[SQLError]]:
    """
    Way - 1
    obj_user = User(name='nietzsche', age=55)
    insert_obj(obj=obj_user)
    ----------------------------------------------------
    Way - 2
    obj_user = User()
    obj_user.name = 'platao'
    obj_user.age = 65
    insert_obj(obj=obj_user)
    """
    try:
        with create_session() as session:
            session.add(obj)
            session.flush()
            updated_obj_data = copy(obj)
            session.commit()
    except IntegrityError as error:
        is_duplicate_entry = "1062 (23000): Duplicate entry" in str(error.orig)
        if is_duplicate_entry:
            return None, SQLError.duplicate_entry
        else:
            raise Exception("IntegrityError SQL error")

    return updated_obj_data, None


def insert_all_obj(objs: list):
    """
    Way - 1
    obj_user1 = User(name='zenao', age=55)
    obj_user2 = User(name='diogenes', age=55)
    insert_all_obj(objs=[obj_user1, obj_user2])
    """
    with create_session() as session:
        session.add_all(objs)
        session.flush()
        updated_obj_data = copy(objs)
        session.commit()

    return updated_obj_data


def update_obj(obj_table, filter_by: dict, obj_update):
    """
    Way - 1
    update_obj(obj=User, filter_by={"id": 1}, obj_update={User.name: 'zabuza', User.age: 50})
    ----------------------------------------------------
    Way - 2
    update_dict = {}
    update_dict[User.name] = 'aristoteles'
    update_dict[User.age] = 48
    update_obj(obj=User, filter_by={"id": 1}, obj_update=update_dict)
    """
    with create_session() as session:
        session.query(obj_table).filter_by(**filter_by).update(obj_update)
        session.flush()
        updated_obj_data = copy(obj_update)
        session.commit()

    return updated_obj_data


def delete_obj(obj_table, filter_by: dict) -> Optional[SQLError]:
    """
    Way - 1
    delete_obj(obj=User, filter_by={"id": 1})
    """
    with create_session() as session:
        qtd_rows = session.query(obj_table).filter_by(**filter_by).delete()
        session.commit()

    if qtd_rows >= 1:
        return None
    else:
        return SQLError.not_found


if __name__ == '__main__':
    ...

    # ------------------------------------- use of create_session -------------------------------------
    # Form - 1
    # with create_session() as session:
    #     var = session.query(User).filter_by(id=2).first()
    #     print(var.name)

    # Form - 2
    # with create_session() as session:
    #     results = session.query(User).all()
    #     for row in results:
    #         print(row.name)

    # ------------------------------------- use of select_obj -------------------------------------
    # var = select_obj(obj=User, filter_by={"id": 1})
    # print(var)

    # ------------------------------------- use of update_obj -------------------------------------
    # Form - 1
    # update_obj(obj=User, filter_by={"id": 1}, obj_update={User.name: 'zabuza', User.age: 50})

    # Form - 2
    # update_dict = {}
    # update_dict[User.name] = 'aristoteles'
    # update_dict[User.age] = 48
    # update_obj(obj=User, filter_by={"id": 1}, obj_update=update_dict)

    # ------------------------------------- use of insert_obj -------------------------------------
    # Form - 1
    # obj_user = User(name='nietzsche', age=55)
    # insert_obj(obj=obj_user)

    # Form - 2
    # obj_user = User()
    # obj_user.name = 'platao'
    # obj_user.age = 65
    # insert_obj(obj=obj_user)

    # ------------------------------------- use of insert_all_obj -------------------------------------
    # Form - 1
    # obj_user1 = User(name='zenao', age=55)
    # obj_user2 = User(name='diogenes', age=55)
    # insert_all_obj(objs=[obj_user1, obj_user2])

    # ------------------------------------- use of delete_obj -------------------------------------
    # delete_obj(obj=User, filter_by={"id": 1})
