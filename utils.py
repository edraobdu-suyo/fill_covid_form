from constants import CITIES_MAP, COVID_TEST_RESULT_MAP, OTHER_CITY_IDX, NO_COVID_RESULT_IDX

def get_city_radio_index(city_name):
    """
    Returns the radio index on the form for the specified city_name
    If it's a city that's not in the list, then we select the option
    # 'Other', which is the raduio button on index number 8.
    """
    try:
        return CITIES_MAP[city_name]
    except KeyError:
        # City is not on the list
        return OTHER_CITY_IDX


def get_covid_test_result_index(test_result):
    """
    Returns the radio index on the form for the specified 
    covid test rresult.
    """
    try:
        return COVID_TEST_RESULT_MAP[test_result]
    except KeyError:
        # City is not on the list
        return NO_COVID_RESULT_IDX

    
def escape_printy(val):
    """
    Takes a value that its gonna be inserted into teh printy function and scape it
    """
    return str(val).replace('[', '\[').replace(']', '\]').replace('@', '\@')