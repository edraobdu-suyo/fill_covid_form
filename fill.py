"""
Follow this tutorial:
https://medium.com/swlh/automatically-filling-multiple-responses-into-a-google-form-with-selenium-and-python-176340c5220d
"""
import os
import sys
import pathlib

from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from printy import printy

from constants import *
from exceptions import InvalidFormType
from utils import (
    get_city_radio_index, 
    get_conditions_index, 
    get_temperature_index,
    escape_printy
)


# Defines whether it's the form from the end of the 
# day or starting the day.
try:
    form_type = sys.argv[1]
    if form_type not in FORM_TYPE_FLAGS:
        raise InvalidFormType('[m>]\'{0}\'@ is not a valid form type, options are: {1}'.format(form_type, escape_printy(FORM_TYPE_FLAGS)))
except IndexError:
    printy('Please use the flags [m>]{0}@ to specify whether it\' the form of the begining of the day or the end of the day'.format(escape_printy(FORM_TYPE_FLAGS)), predefined='r>')
    exit()
except InvalidFormType as e:
    printy(e, predefined='r>')
    exit()    

load_dotenv()

# Set up browser
option = webdriver.ChromeOptions()
for opt in BROWSER_OPTIONS:
    option.add_argument(opt)

browser = webdriver.Chrome(executable_path=os.path.join(pathlib.Path(__file__).parent.absolute(), 'webdriver'))
browser.get(FORM_URL)

# Elements
inputs = browser.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
radiobuttons = browser.find_elements_by_class_name('docssharedWizToggleLabeledLabelWrapper')
nested_inputs = browser.find_elements_by_class_name('quantumWizTextinputSimpleinputInput')

now = datetime.now()

# Email
email_input = inputs[EMAIL_IDX]
email_value = os.getenv('EMAIL', None)
if email_value is not None:
    email_input.send_keys(email_value)

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


# City
city_value = os.getenv('CITY', None)
if city_value is not None:
    city_idx = get_city_radio_index(city_value)
    city_input = radiobuttons[city_idx]
    city_input.click()
    
    # In case it is the 'other' options
    # we send the value of the city
    if city_idx == OTHER_CITY_IDX:
        city_name_input = nested_inputs[OTHER_CITY_NAME_IDX]
        city_name_input.send_keys(city_value)

# Conditions
conditions_value = os.getenv('CONDITIONS', None)
if conditions_value is not None:
    conditions_idx = get_conditions_index(conditions_value)
    conditions_input = radiobuttons[conditions_idx]
    conditions_input.click()
    
    # In case it is the 'other' options
    # we send the value of the conditions
    if conditions_idx == CONDITIONS_OTHER_IDX:
        conditions_text_input = nested_inputs[CONDITIONS_TEXT_IDX]
        conditions_text_input.send_keys(conditions_value)

# Temperature
temperature_value = os.getenv('TEMPERATURE', None)
if temperature_value is not None:
    temperature_idx = get_temperature_index(temperature_value)
    temperature_input = radiobuttons[temperature_idx]
    temperature_input.click()

