from datetime import datetime
from pprint import pprint

from elasticsearch.exceptions import NotFoundError

from elasticsearch import Elasticsearch


def get_elastic() -> Elasticsearch:
    host = 'http://localhost:9200'

    return Elasticsearch(host)


def get_data_by_id():
    es = get_elastic()

    response = es.get(index='index_test', id=2)
    pprint(response['_source'])


def search_data():
    es = get_elastic()

    nome = 'jorge'

    body = {
        "query": {
            "match": {
                "nome": "" + nome + ""
            }

        }
    }

    response = es.search(index='index_test', body=body)
    pprint(response)

    for v in response['hits']['hits']:
        print(v['_source'])


def insert_data():
    es = get_elastic()

    body = {
        "nome": 'jorge',
        "idade": 44,
        "timestamp": datetime.now()}
    response = es.index(index='index_test', id=2, body=body)
    pprint(response['result'])


def delete_data():
    es = get_elastic()

    try:
        response = es.delete(index='index_test', id=2)
        print(response)
    except NotFoundError:
        print('data not found to delete')


if __name__ == '__main__':
    delete_data()
