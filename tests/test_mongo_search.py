from dbmanager.mongo.mongo_search import SimpleSelectionFiler


def test_add_filtering_criteria():
    simple_filter_function = SimpleSelectionFiler()
    simple_filter_function.add_filtering_criteria("sarea", "信義區")

    print(simple_filter_function)