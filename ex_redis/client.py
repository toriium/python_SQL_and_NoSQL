from contextlib import contextmanager

from redis.client import Redis
import redis


@contextmanager
def get_client(db: int = 0) -> Redis:
    try:
        client = redis.Redis(
            host='localhost',
            port=6379,
            db=db,
            password=None
        )
        yield client
    finally:
        client.close()
