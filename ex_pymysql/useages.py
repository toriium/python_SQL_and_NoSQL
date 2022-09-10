from utils import DataBase

if __name__ == '__main__':
    sql = 'select * from planets where id_planet= %s'
    arguments = (5)
    query_result = DataBase.consult_all(sql, arguments)
    print(query_result)
    print(type(query_result))
    if query_result:
        print('tem valor')