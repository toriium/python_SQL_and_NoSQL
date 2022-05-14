# docker run --name my-redis -p 6379:6379 -d redis


import redis

# connect to redis
client = redis.Redis(host='localhost', port=6379)

# set a key
client.set('test-key', 'test-value')

# get a value
value = client.get('test-key')
print(value)