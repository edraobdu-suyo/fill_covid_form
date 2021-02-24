from constants import (
    CITIES_MAP, 
    OTHER_CITY_IDX,
    CONDITIONS_MAP,
    CONDITIONS_OTHER_IDX,
    TEMPERATURE_MAP,
    TEMPERATURE_LOWER_IDX
)

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


def get_conditions_index(conditions):
    try:
        return CONDITIONS_MAP[conditions]
    except KeyError:        
        return CONDITIONS_OTHER_IDX

def get_temperature_index(temp):
    try:
        return TEMPERATURE_MAP[temp]
    except KeyError:
        return TEMPERATURE_LOWER_IDX
    
def escape_printy(val):
    """
    Takes a value that its gonna be inserted into teh printy function and scape it
    """
    return str(val).replace('[', '\[').replace(']', '\]').replace('@', '\@')