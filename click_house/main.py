import clickhouse_connect

PORT = 8123
HOST = "localhost"
USERNAME = "username"
PASSWORD = "password"


CLIENT = clickhouse_connect.get_client(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)

# print(CLIENT.server_version)