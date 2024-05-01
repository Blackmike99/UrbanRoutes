import data
import urban_routes_page
from selenium import webdriver


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        #no lo modifiques, ya que necesitamos un registro adicional habilitado
        #para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.wait_for_page_load()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort(self):
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.taxi_call_button_process()
        routes_page.wait_for_tariff_picker()
        routes_page.comfort_button_click()
        comfort_button_class = data.comfort_button_class
        assert routes_page.check_comfort_button_is_enabled() == comfort_button_class

    def test_phone_number(self):
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.phone_button_click()
        routes_page.wait_for_phone_field()
        phone = data.phone_number
        routes_page.set_phone_number(phone)
        routes_page.add_phone_button_click()
        routes_page.code_process()
        code = routes_page.get_phone_code()
        assert routes_page.get_phone_code() == code
        assert routes_page.get_phone_number() == phone

    def test_add_card(self):
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.add_card_process()
        card = data.card_number
        card_code = data.card_code
        routes_page.set_card_process(card, card_code)
        assert routes_page.get_card_field() == card
        assert routes_page.get_card_code_field() == card_code
        routes_page.link_card_button_click()
        routes_page.wait_for_card_selection_button()
        routes_page.close_card_selection_click()

    def test_send_message(self):
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.set_driver_message(message)
        assert routes_page.get_driver_message() == message

    def test_blanket_and_tissue_slider(self):
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.tissues_slider_click()
        assert routes_page.check_tissues_slider_is_enabled() == True

    def test_ice_cream_button(self):
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        counter_active = data.ice_cream_counter_enabled
        routes_page.ice_cream_counter_click()
        assert routes_page.check_ice_cream_counter_is_enabled() == counter_active

    def test_modal_is_enabled(self):
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.reserve_taxi_click()
        routes_page.wait_for_cancel_reservation_panel()
        reservation_panel_class = data.reservation_panel_class
        assert routes_page.check_reservation_panel_is_enabled() == reservation_panel_class

    def test_driver_information(self):
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.wait_for_driver_information()
        driver_attribute = data.driver_attribute
        assert routes_page.check_driver_information_appears() == driver_attribute

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
