# pruebaTrueHome

Este repositorio se divide en 2 proyectos:
El primero (testSite) alberga a la API con las características solicitadas
El segundo (testWeb) contiene la página web que muestra las entradas de la API

Para iniciar cada proyecto basta con ejecutar las siguienters líneas

python testSite/manager.py runserver localhost:8000

python testWeb/manager.py runserver localhost:8001


# API

Para usar el API se tienen las siguientes urls:

http://localhost:8000/API - Muestra la lista de todos los objetos en la DB (no requiere login) Método GET

http://localhost:8000/API2 - Para añadir un nuevo registro (requiere login) Método POST

http://localhost:8000/API2/? - Para eliminar o modificar un registro (requiere login) Métodos  DELETE, PATCH

# Autenticacion

Las credenciales para realizar el login son:

username= ivan
password= 1234

Se asigna un token con una duración de 15 días.
