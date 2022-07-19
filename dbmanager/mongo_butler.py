
from pymongo import MongoClient


class MongoButler:

    def __init__(self):
        super(MongoButler).__init__()

        self.__mongo_db_url = None
        self.__mongo_db_user = None
        self.__mongo_db_password = None

        # Mongo client going to be built
        self.__mongo_client = None

    def set_url(self, url):
        self.__mongo_db_url = url

    def set_user(self, user):
        self.__mongo_db_user = user

    def set_password(self, password):
        self.__mongo_db_password = password

    def get_mongo_client(self):

        complete_connection_url = self.__mongo_db_url.format(self.__mongo_db_user, self.__mongo_db_password)

        self.__mongo_client = MongoClient(complete_connection_url)

        return self.__mongo_client

    def __str__(self):
        return self.__mongo_db_url



class MongoButlerBuilder:

    def __init__(self, mongo_butler=MongoButler()):

        self.mongo_butler = mongo_butler

    def set_mongo_db_url(self, url):
        self.mongo_butler.set_url(url)
        return self

    def set_mongo_db_user(self, user):
        self.mongo_butler.set_user(user)
        return self

    def set_mongo_db_password(self, password):
        self.mongo_butler.set_password(password)
        return self

    def build(self):
        return self.mongo_butler.get_mongo_client()
