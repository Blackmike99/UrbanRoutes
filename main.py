import data
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(self):
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException

    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in self.driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = self.driver.execute_cdp_cmd('Network.getResponseBody',
                                                   {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue

        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")

        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    urban_logo = (By.CLASS_NAME, 'logo-image')
    personal_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[3]')
    taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[2]/div[3]/img')
    taxi_call_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    tariff_picker = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]')
    comfort_Button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    phone_number_button = (By.CLASS_NAME, "np-button")
    phone_field = (By.ID, 'phone')
    add_phone_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    code_field = (By.XPATH, '//*[@id="code"]')
    code_confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    card_button = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card_button = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_field = (By.ID, 'number')
    card_code_field = (By.XPATH, '//*[@id="code"]')
    message_field = (By.ID, 'comment')
    blanket_and_tissues_slider = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div'
                                            '[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ice_cream_plus_counter = (By.CLASS_NAME, 'counter-plus')
    ice_cream_counter = (By.CLASS_NAME, 'counter-value')
    reserve_taxi_button = (By.CLASS_NAME, 'smart-button')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_phone_number(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_code(self):
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.code_field).send_keys(code)

    def set_card_field(self, card):
        self.driver.find_element(*self.card_field).send_keys(card)

    def set_card_code_field(self, code):
        self.driver.find_element(*self.card_code_field).send_keys(code)

    def set_driver_message(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    def get_phone_code(self):
        return self.driver.find_element(*self.code_field).get_property('value')

    def get_card_field(self):
        return self.driver.find_element(*self.card_field).get_property('value')

    def get_card_code_field(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def get_driver_message(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    """def get_ice_cream_counter(self):
        return self.driver.find_element(*self.ice_cream_counter)"""

    def set_route(self, from_field, to_field):
        self.set_from(from_field)
        self.set_to(to_field)

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.urban_logo))

    def wait_for_personal_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.personal_button))

    def personal_button_click(self):
        self.driver.find_element(*self.personal_button).click()

    def wait_for_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.taxi_button))

    def taxi_button_click(self):
        self.driver.find_element(*self.taxi_button).click()

    def wait_for_taxi_call_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.taxi_call_button))

    def taxi_call_button_click(self):
        self.driver.find_element(*self.taxi_call_button).click()

    def taxi_call_button_process(self):
        self.wait_for_personal_button()
        self.personal_button_click()
        self.wait_for_taxi_button()
        self.taxi_button_click()
        self.wait_for_taxi_call_button()
        self.taxi_call_button_click()

    def wait_for_tariff_picker(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.tariff_picker))

    def check_comfort_button_is_enabled(self):
        return self.driver.find_element(*self.comfort_Button).get_attribute('class')

    def comfort_button_click(self):
        self.driver.find_element(*self.comfort_Button).click()

    def phone_button_click(self):
        self.driver.find_element(*self.phone_number_button).click()

    def wait_for_phone_field(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located(self.phone_field)))

    def add_phone_button_click(self):
        self.driver.find_element(*self.add_phone_button).click()

    def wait_for_code_field(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located(self.code_field)))

    def code_button_click(self):
        self.driver.find_element(*self.code_confirm_button).click()

    def code_process(self):
        self.wait_for_code_field()
        time.sleep(5)
        self.set_code()
        self.code_button_click()

    def card_button_click(self):
        self.driver.find_element(*self.card_button).click()

    def wait_for_add_card_button(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located(self.add_card_button)))

    def add_card_button_click(self):
        self.driver.find_element(*self.add_card_button).click()

    def wait_for_card_field(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located(self.card_field)))

    def tissues_slider_click(self):
        self.driver.find_element(*self.blanket_and_tissues_slider).click()

    def check_tissues_slider_is_enabled(self):
        return self.driver.find_element(*self.blanket_and_tissues_slider).is_enabled()

    def check_ice_cream_counter_is_enabled(self):
        return self.driver.find_element(*self.ice_cream_plus_counter).get_attribute('class')

    def ice_cream_counter_click(self):
        for i in range(2):
            self.driver.find_element(*self.ice_cream_plus_counter).click()

    def reserve_taxi_click(self):
        self.driver.find_element(*self.reserve_taxi_button).click()


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        #no lo modifiques, ya que necesitamos un registro adicional habilitado
        #para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.FIREFOX
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Firefox()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_page_load()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.taxi_call_button_process()
        routes_page.wait_for_tariff_picker()
        routes_page.comfort_button_click()
        assert routes_page.check_comfort_button_is_enabled() == 'tcard active'

    """def test_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.phone_button_click()
        routes_page.wait_for_phone_field()
        phone = data.phone_number
        routes_page.set_phone_number(phone)
        assert routes_page.get_phone_number() == phone
        routes_page.add_phone_button_click()
        routes_page.code_process()
        code = routes_page.get_phone_code()
        assert routes_page.get_phone_code() == code"""

    """def test_card_add(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.card_button_click()
        routes_page.wait_for_add_card_button()
        routes_page.add_card_button_click()
        routes_page.wait_for_card_field()
        card = data.card_number
        card_code = data.card_code
        routes_page.set_card_field(card)
        routes_page.set_card_code_field(card_code)"""

    def test_send_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.set_driver_message(message)
        assert routes_page.get_driver_message() == message

    def test_blanket_and_tissue_slider(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.tissues_slider_click()
        assert routes_page.check_tissues_slider_is_enabled() == True

    def test_ice_cream_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.check_ice_cream_counter_is_enabled() == "counter-plus"
        routes_page.ice_cream_counter_click()
        assert routes_page.check_ice_cream_counter_is_enabled() == "counter-plus disabled"

    def test_modal_is_enabled(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.reserve_taxi_click()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
