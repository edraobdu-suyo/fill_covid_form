"""
Constants to configure the browser
"""

# Add '--headless' and 'disable-gpu' to the list if you want to
# run the browser int he background without GUI.
# BROWSER_OPTIONS = ['-incognito', '--headless', 'disable-gpu']
BROWSER_OPTIONS = ['-incognito']
FORM_URL = 'https://forms.gle/Kp9EereJSibEqNAj6'
DRIVER_PATH = '/home/edgar/Documents/Suyo/fill_covid_form/'

# Form type options flags
START_FLAG = '--start'
END_FLAG = '--end'
FORM_TYPE_FLAGS = [START_FLAG, END_FLAG]

# ELEMENT INDEXES
# Inputs
EMAIL_ONE_IDX = 0
REPORT_DATE_IDX = 1
FULL_NAME_IDX = 2
ID_NUMBER_IDX = 3
EMAIL_TWO_IDX = 4
CONDITIONS_IDX = 5
TEMPERATURE_IDX = 6
HOURS_IDX = 7
MINUTES_IDX = 8
SECONDS_IDX = 9
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
POSITIVE_COVID_RESULT_IDX = 9
NEGATIVE_COVID_RESULT_IDX = 10
NO_COVID_RESULT_IDX = 11
# Nested inputs, like the one in 'Other' city option
OTHER_CITY_NAME_IDX = 0