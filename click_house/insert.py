from client import CLIENT


row1 = [1000, 'String Value 1000', 5.233]
row2 = [2000, 'String Value 2000', -107.04]
data = [row1, row2]
CLIENT.insert('new_table', data, column_names=['key', 'value', 'metric'])