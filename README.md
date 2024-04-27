#Proyecto 7: Proyecto para el septimo sprint: Tarea
#Miguel Alberto De La Torre Rodríguez, grupo 8

###Descripcion

Este documento contiene las pruebas autmatizadas del funcionamiento de la pagina Urban routes al
pedir un taxi.
Las pruebas se hicieron con pytest y selenium en pycharm, haciendo uso de las librerias webdriver,
Keys, By, expected_conditions y WebDriverWait

###retrieve_phone_code

Esta es una funcion auxiliar que ayuda a conseguir el codigo de confirmacion de telefono durante
las pruebas de vinculacion de numero de telefono.

###class UrbanRoutesPage

Es la clase que contiene los elementos de la pagina Urban routes en forma de atributos, asi como
los procedimientos realizados en forma de metodos y pasos.

####Atributos
Cada atributo es un elemento de la página, cada uno buscado de diferente forma mediante el uso de
XPATHS, selectores CSS, IDs y nombres de clase.

####def __init__:
Costructor de la clase UrbanRoutesPage

####def set_from
Obtiene un valor y se lo envía al campo de inicio del viaje

####def set_to:
Obtiene un valor y se lo envía al campo de destino del viaje

####set_phone_number
Obtiene un valor y se lo envía al campo de destino del viaje