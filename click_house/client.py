import clickhouse_connect

PORT = 8123
HOST = "localhost"
USERNAME = "username"
PASSWORD = "password"
DATABASE = "my_database"


CLIENT = clickhouse_connect.get_client(host=HOST, port=PORT, username=USERNAME, password=PASSWORD, database=DATABASE)

print(CLIENT.server_version)