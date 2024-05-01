import helpers
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    urban_logo = (By.CLASS_NAME, 'logo-image')
    personal_button = (By.XPATH, '//div[text()="Personal"]')
    taxi_button = (By.CSS_SELECTOR, 'img[src="/static/media/taxi-active.b0be3054.svg"]')
    taxi_call_button = (By.XPATH, '//button[text()="Pedir un taxi"]')
    tariff_picker = (By.CLASS_NAME, 'tariff-cards')
    comfort_Button = (By.CSS_SELECTOR, 'img[src="/static/media/kids.075fd8d4.svg"]')
    phone_number_button = (By.CLASS_NAME, "np-button")
    phone_field = (By.ID, 'phone')
    add_phone_button = (By.XPATH, '//button[text()="Siguiente"]')
    confirmed_phone_field = (By.CLASS_NAME, 'np-text')
    code_field = (By.ID, 'code')
    code_confirm_button = (By.XPATH, '//button[text()="Confirmar"]')
    card_button = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card_button = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, "input[placeholder='12']")
    link_card_button = (By.XPATH, '//button[text()="Agregar"]')
    close_card_selection = (By.XPATH, "//div[@class='payment-picker open']//button['close-button section-close']")
    card_selection = (By.CLASS_NAME, 'pp-checkbox')
    message_field = (By.ID, 'comment')
    blanket_and_tissues_slider = (By.CSS_SELECTOR, 'span[class="slider round"')
    ice_cream_plus_counter = (By.CLASS_NAME, 'counter-plus')
    ice_cream_counter = (By.CLASS_NAME, 'counter-value')
    reserve_taxi_button = (By.CLASS_NAME, 'smart-button')
    reservation_panel_tittle = (By.XPATH, '//div[text()="Buscar automóvil"]')
    driver_photo = (By.CSS_SELECTOR, 'img[src="/static/media/bender.e90e5089.svg"]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_phone_number(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_code(self):
        code = helpers.retrieve_phone_code(self)
        self.driver.find_element(*self.code_field).send_keys(code)

    def set_card_field(self, card):
        self.driver.find_element(*self.card_field).send_keys(card)

    def set_card_code_field(self, code):
        self.driver.find_element(*self.card_code_field).send_keys(code)
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)

    def set_driver_message(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def get_phone_number(self):
        return self.driver.find_element(*self.confirmed_phone_field).text

    def get_phone_code(self):
        return self.driver.find_element(*self.code_field).get_property('value')

    def get_card_field(self):
        return self.driver.find_element(*self.card_field).get_property('value')

    def get_card_code_field(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def get_driver_message(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def set_route(self, from_field, to_field):
        self.set_from(from_field)
        self.set_to(to_field)

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.urban_logo))

    def wait_for_personal_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.personal_button))

    def wait_for_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.taxi_button))

    def wait_for_taxi_call_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.taxi_call_button))

    def wait_for_tariff_picker(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.tariff_picker))

    def wait_for_phone_field(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located(self.phone_field)))

    def wait_for_code_field(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located(self.code_field)))

    def wait_for_card_selection_button(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located(self.card_selection)))

    def wait_for_card_field(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located(self.card_field)))

    def wait_for_add_card_button(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located(self.add_card_button)))

    def wait_for_cancel_reservation_panel(self):
        WebDriverWait(self.driver, 3).until((expected_conditions.visibility_of_element_located
                                             (self.reservation_panel_tittle)))

    def wait_for_driver_information(self):
        WebDriverWait(self.driver, 35).until((expected_conditions.visibility_of_element_located(self.driver_photo)))

    def comfort_button_click(self):
        self.driver.find_element(*self.comfort_Button).click()

    def phone_button_click(self):
        self.driver.find_element(*self.phone_number_button).click()

    def add_phone_button_click(self):
        self.driver.find_element(*self.add_phone_button).click()

    def code_button_click(self):
        self.driver.find_element(*self.code_confirm_button).click()

    def taxi_button_click(self):
        self.driver.find_element(*self.taxi_button).click()

    def personal_button_click(self):
        self.driver.find_element(*self.personal_button).click()

    def taxi_call_button_click(self):
        self.driver.find_element(*self.taxi_call_button).click()

    def card_button_click(self):
        self.driver.find_element(*self.card_button).click()

    def add_card_button_click(self):
        self.driver.find_element(*self.add_card_button).click()

    def close_card_selection_click(self):
        self.driver.find_element(*self.close_card_selection).click()

    def link_card_button_click(self):
        self.driver.find_element(*self.link_card_button).click()

    def tissues_slider_click(self):
        self.driver.find_element(*self.blanket_and_tissues_slider).click()

    def ice_cream_counter_click(self):
        for i in range(2):
            self.driver.find_element(*self.ice_cream_plus_counter).click()

    def reserve_taxi_click(self):
        self.driver.find_element(*self.reserve_taxi_button).click()

    def taxi_call_button_process(self):
        self.wait_for_personal_button()
        self.personal_button_click()
        self.wait_for_taxi_button()
        self.taxi_button_click()
        self.wait_for_taxi_call_button()
        self.taxi_call_button_click()

    def code_process(self):
        self.wait_for_code_field()
        self.set_code()
        self.code_button_click()

    def add_card_process(self):
        self.card_button_click()
        self.wait_for_add_card_button()
        self.add_card_button_click()
        self.wait_for_card_field()

    def set_card_process(self, card, card_code):
        self.set_card_field(card)
        self.set_card_code_field(card_code)

    def check_tissues_slider_is_enabled(self):
        return self.driver.find_element(*self.blanket_and_tissues_slider).is_enabled()

    def check_ice_cream_counter_is_enabled(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def check_reservation_panel_is_enabled(self):
        return self.driver.find_element(*self.reservation_panel_tittle).get_attribute('class')

    def check_comfort_button_is_enabled(self):
        return self.driver.find_element(*self.comfort_Button).get_attribute('alt')

    def check_driver_information_appears(self):
        return self.driver.find_element(*self.driver_photo).get_attribute("alt")
