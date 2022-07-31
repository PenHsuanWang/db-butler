import pandas

from dbmanager.mongo_butler import MongoClientBuilder, MongoButler
# from dbmanager.mongo.mongo_sink import MongoSink

def test_construction():
    CONNECTION_URL = "mongodb+srv://{}:{}@cathay-mongodb-training.qskew.mongodb.net/?retryWrites=true&w=majority"

    builder = MongoClientBuilder()

    mongo_butler = builder \
        .set_url(CONNECTION_URL) \
        .set_username('pwang') \
        .set_password("pwang") \
        .build()

    info = mongo_butler.server_info()
    print(info)

    assert mongo_butler


def test_mongo_sink():

    CONNECTION_URL = "mongodb+srv://{}:{}@cathay-mongodb-training.qskew.mongodb.net/?retryWrites=true&w=majority"

    mongo_butler = MongoButler(
        connection_url=CONNECTION_URL,
        username='pwang',
        password='pwang'
    )

    DATA_TO_SAVE = {
        'name': 'pwang',
        'age': 28,
        'address': {
            'city': 'taipei',
            'country': 'taiwan',
            'street': 'civil brv.'
                     }
    }

    df = pandas.DataFrame()

    mongo_butler.save_data(data=DATA_TO_SAVE, db_name='test_from_pycharm', collection_name='mongo_sink_unitest')
    print("Save data successfully")




