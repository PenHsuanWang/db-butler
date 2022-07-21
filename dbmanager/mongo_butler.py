from beartype import beartype

import pymongo
from pymongo import MongoClient
from pymongo.errors import OperationFailure


class MongoClientBuilder:

    def __init__(self):
        """
        Initializing MongoClient
        setting the interface to set up mongodb connection information, including:
        mongodb server url
        username
        password
        """

        self.__mongo_db_url = None
        self.__mongo_db_user = None
        self.__mongo_db_password = None

        # Mongo client going to be built
        self.__mongo_client = None

    def _check_mongo_client_is_valid(self):

        try:
            info = self.__mongo_client.server_info()
        except OperationFailure as oerr:
            print("Invalid Username")

    @beartype
    def set_url(self, url: str):
        """
        setup connection url
        :param url:
        :return:
        """
        self.__mongo_db_url = url
        return self

    @beartype
    def set_username(self, user: str):
        """
        setup username
        :param user:
        :return:
        """
        self.__mongo_db_user = user
        return self

    @beartype
    def set_password(self, password: str):
        """
        setup password
        :param password:
        :return:
        """
        self.__mongo_db_password = password
        return self


    def build(self, *args, **kwargs) -> pymongo.MongoClient:

        """
        using provided mongodb connection url and login username, password to initialize mongo client
        :return: MongoClient
        """

        complete_connection_url = self.__mongo_db_url.format(self.__mongo_db_user, self.__mongo_db_password)

        self.__mongo_client = MongoClient(complete_connection_url, **kwargs)
        self._check_mongo_client_is_valid()

        return self.__mongo_client

    def __str__(self):
        return self.__mongo_db_url


class MongoSink:

    def __init__(self):
        self._mongo_client = None

    @beartype
    def save_data(self, data: dict, db_name: str, collection_name: str):
        self._mongo_client[db_name][collection_name].insert_one(data)


class MongoSearch:

    def __init__(self):
        self._mongo_client = None

    @beartype
    def find_data_and_print(self, db_name: str, collection_name: str):
        curser = self._mongo_client[db_name][collection_name].find_one()

        while True:
            try:
                retrive_data = next(curser)
                print(retrive_data)
            except StopIteration:
                print("end of curser")
                break
            except TypeError:
                print(curser.get("address"))
                break


class MongoButler(MongoSink, MongoSearch):

    def __init__(self, connection_url: str, username: str, password: str, **kwargs):

        super(MongoSink).__init__()

        self._mongo_client = MongoClientBuilder() \
            .set_url(connection_url) \
            .set_username(username) \
            .set_password(password) \
            .build(**kwargs)

    def check_databases_list(self):
        print(self._mongo_client.list_database_names())

    # def save_data(self, data: dict, db_name: str, collection_name: str):
    #
    #     self._mongo_client[db_name][collection_name].insert_one(data)




