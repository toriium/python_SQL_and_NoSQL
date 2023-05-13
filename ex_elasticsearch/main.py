from elasticsearch import Elasticsearch


def get_elastic() -> Elasticsearch:
    host = 'http://localhost:9200'

    return Elasticsearch(host)


def insert_data():
    es = get_elastic()

    body = {
        "nome": 'jorge',
        "idade": 44, }
    response = es.index(index='index_test', id=2, body=body)
    print(response['result'])


if __name__ == '__main__':
    insert_data()
