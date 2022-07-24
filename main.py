import pymongo
from pymongo import MongoClient
from dbmanager.mongo_butler import MongoClientBuilder, MongoButler

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # client = MongoClientBuilder()\
    #     .set_url(
    #     "mongodb+srv://{}:{}@cathay-mongodb-training.qskew.mongodb.net/?retryWrites=true&w=majority") \
    #     .set_username('pwang') \
    #     .set_password('pwang') \
    #     .build()
    #
    # print(client.list_database_names())
    #
    # ''' Testing cursor
    # '''
    # db = client.sample_airbnb
    # cursor = db.listingsAndReviews.find({})
    # while True:
    #     try:
    #         data = next(cursor)
    #         print(data)
    #     except StopIteration:
    #         print("end of cursor")
    #         break

    mongo_butler = MongoButler(
        connection_url="mongodb+srv://{}:{}@cathay-mongodb-training.qskew.mongodb.net/?retryWrites=true&w=majority",
        username='pwang',
        password='pwang'
    )

    # data = {"name": "pwang", "age": 28, "address": {"street": "松仁路七號", "city": "台北市", "country": "Taiwan"}}
    # mongo_butler.save_data(data=data, db_name="python_sdk_test", collection_name="person")
    # data = mongo_butler.find_one_data(db_name="youbike_database", collection_name="taipei_youbike_records")
    mongo_butler.find_data_and_print(db_name="youbike_database", collection_name="taipei_youbike_records")
    # print(data)
