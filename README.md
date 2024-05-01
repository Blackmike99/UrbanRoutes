# Proyecto 7: Proyecto para el septimo sprint: Tarea
# Miguel Alberto De La Torre Rodríguez, grupo 8

### Descripción


Este documento contiene las pruebas automatizadas del funcionamiento de la página Urban routes al

pedir un taxi.

Las pruebas se hicieron con pytest y selenium en pycharm, haciendo uso de las librerías webdriver,

Keys, By, expected_conditions y WebDriverWait



- Nota: antes de usar el código, hay que cambiar la URL del archivo data.py a la URL actual, así 

como también tener instalado selenium con su driver de chrome actualizado.

También es necesario tener la librería pytest instalada.



### retrieve_phone_code



Esta es una función auxiliar que ayuda a conseguir el código de confirmación de teléfono durante

las pruebas de vinculación de número de teléfono.



### class UrbanRoutesPage



Es la clase que contiene los elementos de la página Urban routes en forma de atributos, así como

los procedimientos realizados en forma de métodos y pasos.



##### Atributos

Cada atributo es un elemento de la página, cada uno buscado de diferente forma mediante el uso de

XPATHS, selectores CSS, IDs y nombres de clase.



##### def __init__:

Constructor de la clase UrbanRoutesPage.



##### def set_from

Obtiene un valor y se lo envía al campo de inicio del viaje.



##### def set_to:

Obtiene un valor y se lo envía al campo de destino del viaje.



##### set_phone_number

Obtiene un valor y se lo envía al campo de destino del viaje.



##### set_code

Guarda el codigo obtenido mediante la función retrive_phone_code y la envía a la casilla de código

de confirmación de teléfono.



##### set_card_field

Obtiene un valor y se lo envía al campo de número de tarjeta.



##### def set_card_code_field

Obtiene un valor y se lo envía al campo de CVV para luego presionar TAB.



##### def set_driver_message

Obtiene un valor y se lo envía al campo de mensaje para el conductor.



##### def get_from

Retorna el valor actualmente escrito en la casilla de inicio de viaje.



##### def get_to

Retorna el valor actualmente escrito en la casilla de fin de viaje.



##### def get_phone_number

Retorna el valor actualmente escrito en la casilla de número de teléfono.



##### def get_phone_code

Retorna el valor actualmente escrito en la casilla de código de confirmación de teléfono.



##### def get_card_field

Retorna el valor actualmente escrito en la casilla de número de tarjeta.



##### def get_card_code_field

Retorna el valor actualmente escrito en la casilla del CVV.



##### def get_driver_message

Retorna el valor actualmente escrito en la casilla de mensaje para el conductor.



##### def set_route

Recibe 2 valores y le asigna uno al campo de inicio de viaje y el otro al campo de destino.



##### def wait_for_page_load

Espera máximo 3 segundos en lo que el logo de la página es visible antes de empezar.



##### def wait_for_personal_button

Espera máximo 3 segundos en lo que el botón para seleccionar tipo de viaje se hace visible.



##### def wait_for_taxi_button

Espera máximo 3 segundos en lo que el botón para seleccionar tipo de transporte "taxi" se hace visible.



##### def wait_for_taxi_call_button

Espera máximo 3 segundos en lo que el botón para empezar el formulario para pedir un taxi se hace visible.



##### def wait_for_tariff_picker

Espera máximo 3 segundos en lo que el botón para seleccionar tipo de taxi se hace visible.



##### def wait_for_phone_field

Espera máximo 3 segundos en lo que el campo de texto para agregar un número de teléfono se hace visible.



##### def wait_for_code_field

Espera máximo 3 segundos en lo que el campo de texto para agregar el código de confirmación de teléfono

se hace visible.



##### def wait_for_card_selection_button

Espera máximo 3 segundos en lo que el botón para seleccionar tarjeta se hace visible.



##### def wait_for_card_field

Espera máximo 3 segundos en lo que el campo de texto para agregar un número de tarjeta se hace visible.



##### def wait_for_add_card_button

Espera máximo 3 segundos en lo que el botón para agregar tarjeta se hace visible.



##### def wait_for_cancel_reservation_button

Espera máximo 3 segundos en lo que el botón para cancelar el viaje se hace visible.



##### def wait_for_driver_information

Espera máximo 35 segundos en lo que la imagen del conductor se hace visible.



##### def comfort_button_click

Da click sobre el botón de la tarifa comfort.



##### def phone_button_click

Da click sobre el botón para agregar un número de teléfono.



##### def add_phone_button_click

Da click sobre el botón para vincular un número de teléfono.



##### def code_button_click

Da click sobre el botón para confirmar el código de confirmación de teléfono.



##### def taxi_button_click

Da click sobre el botón para abrir la selección de tarifas de taxi.



##### def personal_button_click

Da click sobre el botón para seleccionar libremente el tipo de transporte.



##### def card_button_click

Da click sobre el botón para seleccionar tipo de pago.



##### def add_card_button_click

Da click sobre el botón para agregar una tarjeta.



##### def close_card_selection_click

Da click sobre el botón para cerrar la ventana de selección de tipo de pago.



##### def link_card_button_click

Da click sobre el botón para vincular la tarjeta ingresada.



##### def tissues_slider_click

Da click sobre el slider para incluir una manta y pañuelos.



##### def ice_cream_counter_click

Da 2 clicks sobre el botón para agregar un bote de helado.



##### def reserve_taxi_click

Da click sobre el botón para reservar un taxi.



##### def taxi_call_button_process

Un paso que reúne los métodos wait_for_personal_button,personal_button_click, wait_for_taxi_button

taxi_button_click, wait_for_taxi_call_button y taxi_call_button_click para realizarlos en orden.



##### def code_process

Un paso que reúne los métodos wait_for_code_field, set_code y code_button_clickpara realizarlos en

orden.



##### def add_card_process

Un paso que reúne los métodos card_button_click, wait_for_add_card_button, add_card_button_click

y wait_for_card_field para realizarlos en orden.



##### def set_card_process

Paso para el llenado de campos de tarjeta.



##### def check_tissues_slider_is_enabled

Checa sé el slider de manta y pañuelos está activado.



##### def check_ice_cream_counter_is_enabled

Checa que el botón de helados exista mediante la comparación del nombre de su clase con la actual.



##### def check_reservation_details_button_is_enabled

Checa que el botón de reserva exista mediante la comparación del nombre de su clase con la actual.



##### def check_comfort_button_is_enabled

Checa que el botón de la tarifa comfort exista mediante la comparación de su atributo 'alt' con el actual.



##### def check_driver_information_appears

Checa que la imagen del conductor exista mediante la comparación del nombre de su clase con la actual.



### class TestUrbanRoutes

clase que ayuda a crear la instancia de la página y a realizar las pruebas de esta.



##### def setup_class

método de clase que ayuda a modificar atributos de la clase



##### def test_set_route

Caso de prueba de llenado de los campos from y to.

Esta prueba crea un objeto de página en el cual esperará a que aparezca el logo para después rellenar

los campo de entrada de from y to con las direcciones almacenadas en el archivo data.py, previamente

almacenadas en 2 variables. Una vez hecho esto, el programa probará que la información ingresada coincida

con la información extraída de data.py.



##### def test_select_comfort

Esta prueba usa el objeto previamente creado para buscar el botón de selección de tarifa personal y presionarlo.

Luego, buscara el botón de taxi como transporte y también lo presionará, esto activará un panel que la prueba

va a esperar. Una vez que el panel sea visible, buscará y presionara el botón de la tarifa comfort, asegurándose

de que esté sea el botón buscado comparando el nombre de clase con el nombre de clase real.

Una vez realizada la prueba, buscará y presionará el botón pedir taxi.



##### def test_phone_number

Esta prueba usa el objeto previamente creado para dar click en el botón para abrir el formulario para agregar un

teléfono. Después, esperará a que sea visible la casilla para ingresar el número e ingresara el número 

almacenado en data.py. Una vez ingresado el dato, se comparará con el valor extraído de data.py para después

dar click en el botón para vincular el número. Luego se abrirá la página de confirmación la cual esperá buscando

la casilla de código de confirmación e ingresará el código obtenido mediante el método get_phone_code. 

Una vez llenada la casilla, comparará el código ingresado con el código extraído almacenado en una variable

y dará click en el botón de confirmar.



##### def test_add_card(self):

Esta prueba usa el objeto previamente creado para dar click en el botón de selección de método de pago. Una vez 

hecho esto, esperará la visualización del botón para agregar una nueva tarjeta y esperará la visualización de la

casilla de número de tarjeta para ingresar el número y CVV guardados en data.py y almacenarlos en una variable.

Posteriormente se compararán los valores ingresados con los extraídos de data.py y tabulará antes de dar click

en el botón confirmar.

Una vez hecho esto, esperará la visualización del botón para cerrar la selección de método de pago y le dará click.



##### def test_send_message

Esta prueba usa el objeto previamente creado para almacenar el mensaje para el conductor almacenado en

 data.py en una variable e ingresarlo en la casilla para enviarle un mensaje al conductor. Después, 

comparará el dato ingresado con el de la variable.



##### def test_blanket_and_tissue_slider

Esta prueba usa el objeto previamente creado para dar click en el slider de manta y pañuelos y comprobar que este

esté habilitado.



##### def test_ice_cream_button

Esta prueba usa el objeto previamente creado para comparar el nombre de clase del botón para agregar helado

con 2 nombres de clase localizados en data.py los cuales se guardan en variables locales. una se compara antes 

de hacer click y otro después al este solo poder estar activo si no se han agregado 2 helados.



##### def test_modal_is_enabled

Esta prueba usa el objeto previamente creado para dar click en el botón para reservar un taxi y esperar a 

que aparezca el botón para cancelar un viaje, una vez que es visible, comprueba que si sea el elemento 

comparándolo con el nombre de clase guardado en data.py previamente almacenado en una variable.



##### def test_driver_information

Esta prueba usa el objeto previamente creado para esperar por máximo 35 segundos a que la imagen del conductor 

sea visible, una vez que lo es, comprueba que si sea el elemento comparándolo con el nombre de clase guardado

en data.py previamente almacenado en una variable.



##### def teardown_class

Destruye la instancia