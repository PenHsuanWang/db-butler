from dbmanager.mongo_butler import MongoClientBuilder


def test_construction():
    CONNECTION_URL = "mongodb+srv://{}:{}@cathay-mongodb-training.qskew.mongodb.net/?retryWrites=true&w=majority"

    builder = MongoClientBuilder()

    mongo_client = builder \
        .set_url(CONNECTION_URL) \
        .set_username('123') \
        .set_password("pwang") \
        .build(serverSelectionTimeoutMS=1)

    info = mongo_client.server_info()
    print(info)

    assert mongo_client
