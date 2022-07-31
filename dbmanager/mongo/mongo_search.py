from beartype import beartype


class SimpleSelectionFiler(dict):

    def __init__(self, val=None):

        if val is None:
            val = {}
        super().__init__(val)



    def add_filtering_criteria(self, key: str, value: object):
        """
        add new selection criteria
        :param key:
        :param value:
        :return:
        """
        self[key] = value
        return self


class MongoSearch:

    def __init__(self):
        print("Print from Mongo Search Class")
        self._mongo_client = None

        self._filter_criteria = {}

    @beartype
    def find_one_data(self, db_name: str, collection_name: str):
        data = self._mongo_client[db_name][collection_name].find_one()
        return data

    @beartype
    def find_data_and_print(self, db_name: str, collection_name: str):
        print("invoking finding method from separation class")
        curser = self._mongo_client[db_name][collection_name].find({"sarea": "信義區"})

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