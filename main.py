import pymongo
from pymongo import MongoClient
from dbmanager.mongo_butler import MongoClientBuilder, MongoButler

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    """
    Full run of mongo butler
    Saving data and extraction data from DB.
    """

    mongo_butler = MongoButler(
        connection_url="mongodb+srv://{}:{}@cathay-mongodb-training.qskew.mongodb.net/?retryWrites=true&w=majority",
        username='pwang',
        password='pwang'
    )

    # data = {"name": "pwang", "age": 29, "address": {"street": "松仁路七號", "city": "台北市", "country": "Taiwan"}}
    # mongo_butler.save_data(data=data, db_name="python_sdk_test", collection_name="person")
    # data = mongo_butler.find_one_data(db_name="youbike_database", collection_name="taipei_youbike_records")

    mongo_butler.add_filtering_criteria("sarea", "大安區")
    mongo_butler.find_data_and_print(db_name="youbike_database", collection_name="taipei_youbike_records")
    # print(data)
