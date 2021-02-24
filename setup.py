import os
import dotenv
from printy import printy, inputy

from utils import escape_printy
from constants import *

env_file = dotenv.find_dotenv()
dotenv.load_dotenv(env_file)

# Current values
email = os.getenv('EMAIL', '')
full_name = os.getenv('FULLNAME', '')
id_number = os.getenv('ID_NUMBER', '')
city = os.getenv('CITY', '')
conditions = os.getenv('CONDITIONS_QUESTION', '')
covid_test = os.getenv('COVID_TEST_RESULT', '')
temperature = os.getenv('TEMPERATURE', '')

printy('''
A continuación se presentarán una serie de preguntas, si esta pregunta ya contiene una respuesta, 
se mostrará entre paréntesis al final de la pregunta. Presiona ENTER para mantener la respuesta anterior.
''', 'y')

new_email = inputy('Correo electrónico ([In>]{}@):\n'.format(escape_printy(email)), predefined='b>')

new_full_name = inputy('Nombres y apellidos ([In>]{}@):\n'.format(escape_printy(full_name)), predefined='b>')

new_id_number = inputy('Nº Cédula ([In>]{}@):\n'.format(escape_printy(id_number)), predefined='b>')

new_city = inputy(
    'Ciudad donde reside ([In>]{}@):\n'.format(escape_printy(city)),
    predefined='b>',
    options=list(CITIES_MAP.keys())
)
if new_city == 'Otro':
    new_city = inputy('Especifique el nombre de la ciudad: ', predefined='c>')

new_conditions = inputy('''
Convive con personas mayores de 60 años o con población considerada como 
vulnerable para covid-19, presenta dolor de garganta, malestar general 
o dolor muscular, fiebre (+37.5º), tos, dificultad respiratoria, perdida del 
olfato, ha tenido diarrea o dolor estomacal, ha tenido contacto con 
alguna persona sospechosa para covid-19. *si - *no, amplié su respuesta en 
caso de ser afirmativa alguna de las condiciones mencionadas: ([In>]{}@):
'''.format(escape_printy(conditions)),
    options=list(CONDITIONS_MAP.keys()),
    predefined='b>'
)
if new_conditions == 'Otro':
    new_conditions = inputy('Especifique: ', predefined='c>')

new_temperature = inputy(
    'Temperatura ([In>]{}@):\n'.format(escape_printy(temperature)),
    options=list(TEMPERATURE_MAP.keys()),
    predefined='b>'
)

# Establecemos las variables
dotenv.set_key(env_file, 'EMAIL', new_email or email)
dotenv.set_key(env_file, 'FULLNAME', new_full_name or full_name)
dotenv.set_key(env_file, 'ID_NUMBER', new_id_number or id_number)
dotenv.set_key(env_file, 'CITY', new_city or city)
dotenv.set_key(env_file, 'CONDITIONS', new_conditions or conditions)
dotenv.set_key(env_file, 'TEMPERATURE', new_temperature or temperature)