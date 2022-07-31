from beartype import beartype

import pymongo
from pymongo import MongoClient
from pymongo.errors import OperationFailure


from dbmanager.mongo.mongo_sink import MongoSink
from dbmanager.mongo.mongo_search import MongoSearch


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


class MongoButler(MongoSink, MongoSearch):

    def __init__(self, connection_url: str, username: str, password: str, **kwargs):

        """
        Mongo Butler is designed for other application to invoke mongo db more easily.
        encapsulate pymongo sdk into single interface, people just need to prepare their data or ready to implement the
        data using logic. The I/O from local program to mongoDB is handling by this butler.

        Initializing the Mongo Butler at first. The mongo clint will be built internally using `MongoClientBuilder`.
        Every database client connection is handling by builder. user just need to provide the connection parameters.

        Desire usage of Mongo Butler as following.

        >> mongo_db = MongoButler(
        >>     connection_url="mongodb+srv://{}:{}@cathay-mongodb-training.qskew.mongodb.net/?retryWrites=true&w=majority",
        >>     username='user',
        >>     password='password'
        >> )

        :param connection_url:
        :param username:
        :param password:
        :param kwargs:
        """

        super().__init__()

        self._mongo_client = MongoClientBuilder() \
            .set_url(connection_url) \
            .set_username(username) \
            .set_password(password) \
            .build(**kwargs)

    def check_databases_list(self):
        print(self._mongo_client.list_database_names())





