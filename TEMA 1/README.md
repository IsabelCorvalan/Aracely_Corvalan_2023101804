Descripción

Este proyecto es una página web desarrollada con Flask (framework de Python) que se conecta a una base de datos MySQL. Permite crear, leer, actualizar y eliminar datos (CRUD) desde la web.

Estructura del Proyecto
proyecto_flask_mysql/
│
├── app.py               # Archivo principal de Flask
├── templates/           # Carpeta con archivos HTML
│   ├── index.html
│   └── formulario.html
├── static/              # Carpeta con archivos CSS, JS, imágenes
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Este archivo

Requisitos Previos

Antes de ejecutar el proyecto, necesitas tener instalados:

Python 3.x

MySQL Server

Pip (gestor de paquetes de Python)

Instalación de Dependencias

Dentro de la carpeta del proyecto, ejecuta:

pip install -r requirements.txt


El archivo requirements.txt debe incluir al menos:

Flask
mysql-connector-python

Configuración de la Base de Datos

Abre MySQL y crea la base de datos:

CREATE DATABASE nombre_de_tu_base;


Crea la tabla(s) necesarias según tu proyecto:

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(50)
);


Configura la conexión en app.py:

db = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="nombre_de_tu_base"
)

Ejecutar la Aplicación

Dentro de la carpeta del proyecto, ejecuta:

python main.py


Por defecto, Flask correrá en http://127.0.0.1:5000/.

Abre tu navegador y visita esa dirección para ver tu página web.

Archivos HTML

index.html: Página principal con listado de datos.

formulario.html: Página para ingresar o editar datos.

Notas Adicionales

Asegúrate de que MySQL esté corriendo antes de iniciar Flask.

Si cambias el puerto o host, actualiza la línea:

app.run(debug=True, host='0.0.0.0', port=5000)