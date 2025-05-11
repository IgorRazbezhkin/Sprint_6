from locators.order import Order


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def click_order_button(self):
        self.driver.find_element(*Order.order_button_at_the_top_of_the_page).click()

    def fill_name(self, name):
        self.driver.find_element(*Order.field_name).send_keys(name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*Order.last_name_field).send_keys(last_name)

    def fill_address(self, address):
        self.driver.find_element(*Order.address_field).send_keys(address)

    def select_metro_station(self):
        self.driver.find_element(*Order.field_metro_station).click()
        self.driver.find_element(*Order.metro_station_1).click()

    def fill_phone(self, phone):
        self.driver.find_element(*Order.phone_field).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*Order.next_button).click()

    def select_date(self):
        self.driver.find_element(*Order.field_when_to_bring_scooter).click()
        self.driver.find_element(*Order.date).click()

    def select_rental_period(self):
        self.driver.find_element(*Order.rental_period_field).click()
        self.driver.find_element(*Order.rental_period).click()

    def select_scooter_color(self):
        self.driver.find_element(*Order.scooter_color_field).click()
        self.driver.find_element(*Order.scooter_color_black).click()

    def fill_comment(self, comment):
        self.driver.find_element(*Order.comment_field).send_keys(comment)

    def click_order_button_final(self):
        self.driver.find_element(*Order.order_button).click()

    def confirm_order(self):
        self.driver.find_element(*Order.yes_button).click()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")