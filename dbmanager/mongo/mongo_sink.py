from beartype import beartype
import pandas
from enum import Enum


class SinkDataCasting(Enum):

    def __init__(self):
        super(SinkDataCasting).__init__()
        PANDAF_DF = type(pandas.DataFrame)
        DICT = type(dict)




class MongoSink:

    def __init__(self):
        print("initialization of Abstraction Mongo Sink")
        self._mongo_client = None

    # @beartype
    # def save_data(self, data, db_name: str, collection_name: str):


if __name__ == '__main__':
    enum_data_type = SinkDataCasting()
    print(enum_data_type.DICT)
