#Proyecto 7: Proyecto para el septimo sprint: Tarea
#Miguel Alberto De La Torre Rodríguez, grupo 8

###Descripcion

Este documento contiene las pruebas autmatizadas del funcionamiento de la pagina Urban routes al
pedir un taxi.
Las pruebas se hicieron con pytest y selenium en pycharm, haciendo uso de las librerias webdriver,
Keys, By, expected_conditions y WebDriverWait

-Nota: antes de usar el código, hay que cambiar la URL del archivo data.py a la URL actual, así 
como también tener instalado selenium con su driver de chrome actualizado.
Tambien es necesario tener la librería pytest instalada.

###retrieve_phone_code

Esta es una funcion auxiliar que ayuda a conseguir el codigo de confirmacion de telefono durante
las pruebas de vinculacion de numero de telefono.

###class UrbanRoutesPage

Es la clase que contiene los elementos de la pagina Urban routes en forma de atributos, asi como
los procedimientos realizados en forma de metodos y pasos.

#####Atributos
Cada atributo es un elemento de la página, cada uno buscado de diferente forma mediante el uso de
XPATHS, selectores CSS, IDs y nombres de clase.

#####def __init__:
Costructor de la clase UrbanRoutesPage

#####def set_from
Obtiene un valor y se lo envía al campo de inicio del viaje

#####def set_to:
Obtiene un valor y se lo envía al campo de destino del viaje

#####set_phone_number
Obtiene un valor y se lo envía al campo de destino del viaje

#####set_code
Guarda el codigo obtenido mediante la funcion retrive_phone_code y la envía a la casilla de codigo
de confirmacion de telefono

#####set_card_field
Obtiene un valor y se lo envía al campo de numero de tarjeta

#####def set_card_code_field
Obtiene un valor y se lo envía al campo de CVV para luego presionar TAB

#####def set_driver_message
Obtiene un valor y se lo envía al campo de mensaje para el conductor

#####def get_from
Retorna el valor actualmente escrito en la casilla de inicio de viaje

#####def get_to
Retorna el valor actualmente escrito en la casilla de fin de viaje

#####def get_phone_number
Retorna el valor actualmente escrito en la casilla de número de teléfono

#####def get_phone_code
Retorna el valor actualmente escrito en la casilla de código de confirmacion de teléfono

#####def get_card_field
Retorna el valor actualmente escrito en la casilla de número de tarjeta

#####def get_card_code_field
Retorna el valor actualmente escrito en la casilla del CVV

#####def get_driver_message
Retorna el valor actualmente escrito en la casilla de mensaje para el conductor

#####def set_route
Recibe 2 valores y le asigna uno al campo de inicio de viaje y el otro al campo de destino

#####def wait_for_page_load
Espera máximo 3 segundos en lo que el logo de la pagina es visible antes de empezar

#####

#####

#####

#####

#####
