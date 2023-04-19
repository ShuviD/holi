# Manual del API RUC
La siguiente API proporciona un registro de la SUNAT a traves de la busqueda por RUC.
### Requerimientos
**-Docker
-Python 3.10**
### Creación de una imagen de postgresql en docker
-Abre una terminal

-Descargar la imagen de postgres con el siguiente comando: **docker pull  postgres:15.2 **

-Crear un contenedor con el siguiente comando:  **docker run -p 5432:5432 --name nombre_del_contenedor -v ubicación_del_contenedor\nombre_del_contenedor:/var/lib/postgresql/data -e POSTGRES_PASSWORD=contraseña -d postgres**

-Descargar la db de : https://drive.google.com/file/d/1h5tCGAvsv0S0DoJM-ObaCblYtHwsin3i/view?usp=share_link

-Copiar la db al contenedor que se creo:  **docker cp ruta_del_archivo_en_el_host nombre_del_contenedor:ruta_destino_en_el_contenedor**

-Ingresar a: **docker exec -it nombre_del_contenedor psql -U postgres**
-Crear una base de datos con el comando: **CREATE DATABASE nombre_de_la_db;**

### Instalación
-Abre una terminal
-Clonar el repositorio en el directorio deseado con el comando: **git clone https://github.com/babyraul/APIRUC.git **
-Crea una carpeta
-Navega hasta la carpeta creada en una terminal y crear un entorno virtual de Python con el comando: **python -m venv env**
-Activa el entorno virtual con el comando: **source env/bin/activate (en Linux/Mac) o env\Scripts\activate (en Windows).**
-Instalar las dependencias del proyecto con el siguiente comando: **pip install -r requirements.txt**

### Configuración en el archivo settings.py

Se debe configurar de acuerdo a lo que se creo en su base de datos

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_db',
        'USER': 'usurio_de_la_db',
        'PASSWORD': 'contraseña_de_la_db',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


### Migraciones
-Abre una terminal
-Dirígete a la carpeta ruc y crea las migraciones con el comando: **python manage.py makemigrations consultas_app**
-Aplica las migraciones con el comando:** python manage.py migrate**

### Importar los registros a la base de datos
-Abre una terminal

-Ingresa a la base de datos con el comando: **docker exec -it nombre_del_contenedor psql -U postgres nombre_de_la_basededatos**

-Configurar la codificación de caracteres que se usará para la conexión actual:  S**ET client_encoding = 'LATIN1';**

-Importa la base de datos:** COPY nombre_de_la_tabla FROM '/var/lib/postgresql/data/db.txt' DELIMITER '|';**

-Comprueba que se haya importado:** SELECT * FROM nombre_de_la_tabla;**

### Crear contendor para la API
-abrir el archivo dockerfile
-abre una terminal y navega hasta el proyecto **ruc**
-ejecutar el siguiente comando para crear una imagen:  **docker build -t nombre_de_imagenAPI . **
-crear el contenedor con el siguiente comando: **docker run --name nombre-del-contenedor -p 8000:8000 nombre-de-la-imagen**

### Ejecuciòn
-Abre una terminal
- Ejecutar ambos contenedores con el siguiente comando:  docker start nombre_del_contenedor
-verificar que los contenedores esten ejecutandose: docker ps -a
- Iniciar la api con el siguiente comando(se tiene que estar dentro de la ruta del proyecto(**ruc**)): python manage.py runserver

### Ejemplos de uso:
http://127.0.0.1:8000/consultas/ruc/XXXXXXXXXXX/
Si el RUC existe en la base de datos se mostrará algo similar:
{
    "RUC": "XXXXXXXXXXX",
    "Razon_social": "EMPRESA AS",
    "Estado_del_contribuyente": "ACTIVO",
    "Condicion_de_domicilio": "HABIDO",
    "Ubigeo": "YYYYYY",
    "direccion": "AV. ********"
}

Si la RUC no existe se mostrara un mesaje similar:
**La RUC no fue encontrada**

### Funcionamiento

El archivo ruc_db.txt contiene información sobre el Registro Único de Contribuyentes (RUC) en Perú. La aplicación permite consultar información de un RUC específico mediante su número. Al ingresar el número de RUC en la URL, la aplicación buscará en la base de datos y devolverá la información correspondiente. Si el RUC no está en la base de datos, se devolverá un mensaje de error.

La aplicación llamada consultas_app, tiene un modelo llamado rucs que representa la información de cada RUC. La vista mostrar_ruc se encarga de buscar el RUC en la base de datos y devolver la información correspondiente en formato JSON. El archivo urls.py define la URL para acceder a la vista.