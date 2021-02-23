from constants import (
    CACERES_CITY_IDX, MEDELLIN_CITY_IDX, BOGOTA_CITY_IDX,
    BARRANQUILA_CITY_IDX, TUMACO_CITY_IDX, CAUCASIA_CITY_IDX, 
    OTHER_CITY_IDX, POSITIVE_COVID_RESULT_IDX, NEGATIVE_COVID_RESULT_IDX,
    NO_COVID_RESULT_IDX
)

# It maps the city names on the form with the
# radio button possition in the form
CITIES_MAP = {
    'Caceres': CACERES_CITY_IDX,
    'Medellin': MEDELLIN_CITY_IDX,
    'Bogota': BOGOTA_CITY_IDX,
    'Barranquilla': BARRANQUILA_CITY_IDX,
    'Tumaco': TUMACO_CITY_IDX,
    'Caucasia': CAUCASIA_CITY_IDX
}


COVID_TEST_RESULT_MAP = {
    'Positivo': POSITIVE_COVID_RESULT_IDX,
    'Negativo': NEGATIVE_COVID_RESULT_IDX,
    'No aplica': NO_COVID_RESULT_IDX
}

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