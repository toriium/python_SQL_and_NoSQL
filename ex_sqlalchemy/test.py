from models import User
from orm_utils import insert_obj, delete_obj,update_obj ,select_first_obj,select_all_obj

# Way - 1
# user = User(name="jere")
# insert_obj(user)
# ----------------------------------------------------
# Way - 2
# obj_user = User()
# obj_user.name = 'platao'
# obj_user.age = 65
# result, err = insert_obj(obj=obj_user)
# print(result.name)

# err = delete_obj(obj_table=User, where_clauses=[User.id != 1])


# result = select_all_obj(obj_table=User, where_clauses=[User.id == 1, User.id != 2])
# print(result)

result = select_first_obj(obj_table=User, where_clauses=[User.id==1])
print("before:", result)


result = select_first_obj(obj_table=User, where_clauses=[User.id==1])
print("after:", result)
