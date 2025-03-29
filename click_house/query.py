from client import CLIENT

result = CLIENT.query('SELECT max(key), avg(metric) FROM new_table')


print(result.result_rows)