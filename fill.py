"""
Follow this tutorial:
https://medium.com/swlh/automatically-filling-multiple-responses-into-a-google-form-with-selenium-and-python-176340c5220d
"""
import os
import sys

from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from constants import *
from exceptions import InvalidFormType
from utils import get_city_radio_index, get_covid_test_result_index


# Defines whether it's the form from the end of the 
# day or starting the day.
try:
    form_type = sys.argv[1]
    if form_type not in FORM_TYPE_FLAGS:
        raise InvalidFormType('\'{0}\' is not a valid form type, options are: {1}'.format(form_type, FORM_TYPE_FLAGS))
except IndexError:
    print('Please use the flags {0} to specify whether it\' the form of the begining of the day or the end of the day'.format(FORM_TYPE_FLAGS))
    exit()
except InvalidFormType as e:
    print(e)
    exit()    

load_dotenv()

# Set up browser
option = webdriver.ChromeOptions()
for opt in BROWSER_OPTIONS:
    option.add_argument(opt)

browser = webdriver.Chrome(executable_path=os.path.join(DRIVER_PATH, 'chromedriver'))
browser.get(FORM_URL)

# Elements
inputs = browser.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
radiobuttons = browser.find_elements_by_class_name('docssharedWizToggleLabeledLabelWrapper')
nested_inputs = browser.find_elements_by_class_name('quantumWizTextinputSimpleinputInput')

now = datetime.now()

# Email One
email_one_input = inputs[EMAIL_ONE_IDX]
email_one_value = os.getenv('EMAIL', None)
if email_one_value is not None:
    email_one_input.send_keys(email_one_value)

# Daily Report type
if form_type == START_FLAG:
    daily_report_radio_input = radiobuttons[0]        
else:
    daily_report_radio_input = radiobuttons[1]
daily_report_radio_input.click()

# Report Date
report_date_input = inputs[REPORT_DATE_IDX]
report_date_input.send_keys(now.strftime('%m%d%Y'))

# Full name
full_name_input = inputs[FULL_NAME_IDX]
full_name_value = os.getenv('FULLNAME', None)
if full_name_value is not None:
    full_name_input.send_keys(full_name_value)

# ID Number
id_number_input = inputs[ID_NUMBER_IDX]
id_number_value = os.getenv('ID_NUMBER', None)
if id_number_value is not None:
    id_number_input.send_keys(id_number_value)

# Email Two
email_two_input = inputs[EMAIL_TWO_IDX]
email_two_value = os.getenv('EMAIL', None)
if email_two_value is not None:
    email_two_input.send_keys(email_one_value)

# City
city_value = os.getenv('CITY', None)
if city_value is not None:
    city_idx = get_city_radio_index(city_value)
    city_input = radiobuttons[city_idx]
    city_input.click()
    
    # In case it is the 'other' options
    # we send the value of the city
    city_name_input = nested_inputs[OTHER_CITY_NAME_IDX]
    city_name_input.send_keys(city_value)

# Conditions question
condition_input = inputs[CONDITIONS_IDX]
condition_value = os.getenv('CONDITIONS_QUESTION', None)
if condition_value is not None:
    condition_input.send_keys(condition_value)

# Covid Test
covid_test_value = os.getenv('COVID_TEST_RESULT', None)
if covid_test_value is not None:
    covid_test_idx = get_covid_test_result_index(covid_test_value)
    covid_test_input = radiobuttons[covid_test_idx]
    covid_test_input.click()

temperature_input = inputs[TEMPERATURE_IDX]
temperature_value = os.getenv('TEMPERATURE', None)
if temperature_value is not None:
    temperature_input.send_keys(temperature_value)

# Current hour
inputs[HOURS_IDX].send_keys(str(now.hour))
inputs[MINUTES_IDX].send_keys(str(now.minute))
inputs[SECONDS_IDX].send_keys(str(now.second))
    