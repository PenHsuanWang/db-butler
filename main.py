import pymongo
from pymongo import MongoClient
from dbmanager.mongo_butler import MongoButlerBuilder

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # client = MongoClient("mongodb+srv://pwang:pwang@cathay-mongodb-training.qskew.mongodb.net/?retryWrites=true&w=majority")
    client = MongoButlerBuilder()\
        .set_mongo_db_url(
        "mongodb+srv://{}:{}@cathay-mongodb-training.qskew.mongodb.net/?retryWrites=true&w=majority") \
        .set_mongo_db_user('pwang') \
        .set_mongo_db_password('pwang') \
        .build()

    print(client.list_database_names())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
