"""
Constants to configure the browser
"""

# Add '--headless' and 'disable-gpu' to the list if you want to
# run the browser int he background without GUI.
# BROWSER_OPTIONS = ['-incognito', '--headless', 'disable-gpu']
BROWSER_OPTIONS = ['-incognito']
FORM_URL = 'https://forms.gle/Kp9EereJSibEqNAj6'

# Form type options flags
START_FLAG = '--start'
END_FLAG = '--end'
FORM_TYPE_FLAGS = [START_FLAG, END_FLAG]

# ELEMENT INDEXES
# Inputs
EMAIL_IDX = 0
REPORT_DATE_IDX = 1
FULL_NAME_IDX = 2
ID_NUMBER_IDX = 3

# radio buttons
DAILY_REPORT_START_IDX = 0
DAILY_REPORT_END_IDX = 1
CACERES_CITY_IDX = 2
MEDELLIN_CITY_IDX = 3
BOGOTA_CITY_IDX = 4
BARRANQUILA_CITY_IDX = 5
TUMACO_CITY_IDX = 6
CAUCASIA_CITY_IDX = 7
OTHER_CITY_IDX = 8
CONDITIONS_NO_IDX = 9
CONDITIONS_OTHER_IDX = 10
TEMPERATURE_LOWER_IDX = 11
TEMPERATURE_HIGHER_IDX = 12

# Nested inputs, like the one in 'Other' city option
OTHER_CITY_NAME_IDX = 0
CONDITIONS_TEXT_IDX = 1


# It maps the city names on the form with the
# radio button possition in the form
CITIES_MAP = {
    'Caceres': CACERES_CITY_IDX,
    'Medellin': MEDELLIN_CITY_IDX,
    'Bogota': BOGOTA_CITY_IDX,
    'Barranquilla': BARRANQUILA_CITY_IDX,
    'Tumaco': TUMACO_CITY_IDX,
    'Caucasia': CAUCASIA_CITY_IDX,
    'Otro': OTHER_CITY_IDX
}


CONDITIONS_MAP = {
    'No': CONDITIONS_NO_IDX,
    'Otro': CONDITIONS_OTHER_IDX,    
}

TEMPERATURE_MAP = {
    'Inferior a 37.4°': TEMPERATURE_LOWER_IDX,
    'Superior a 37.5°': TEMPERATURE_HIGHER_IDX
}