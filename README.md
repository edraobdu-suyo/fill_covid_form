# AUTO DILIGENCIAMIENTO FORMULARIO COVID

## Demostración

https://www.loom.com/share/8519d64d30614339abaf9f73c2674fee

## Configuración

Una vez el repositorio ha sido clonado:

1. Crea un entorno virtual e instalas las dependencias listadas en el archivo
requirements.txt

    ```bash
    cd ~/path_to_your_virtual_environments/       
    virtualenv -p python3 fill_form
    source fill_form/bin/activate

    cd ~/path_to_the_cloned_repo
    pip install requirements.txt
    ```

2. Descarga el WebDriver para Google Chrome de acuerdo a su versión. El
    actual repositorio contiene el WebDriver para Google Chrome versión `88.0.4324`, llamado `webdriver`. Es importante que el archivo que descarges sea guardado en la raíz del repositorio y cuyo nombre sea siempre `webdriver`.

    link para webdrivers de Google Chrome: https://chromedriver.chromium.org/downloads

3. Ejecuta el script `setup.py` para configurar las variables de entorno que se usarán para el diligenciamiento del formulario:

    ```bash
    # Ejecutalo en la raíz del repositorio
    python setup.py
    ```

## Ejecutar

Ejecuta el script `fill.py` el cual toma un argumento obligatorio: las opcionas `--start` o `--end` las cuales indicarán si el formulario se está diligenciando al iniciar la jornada laboral, o al finalizar:

```bash
# Al inicio de la jornada laboral
python fill.py --start

# Al final de la jornada laboral
python fill.py --end
```