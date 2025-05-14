from locators.order import Order
from pages.base_page import BasePage


class OrderPage(BasePage):

    def click_order_button(self):
        self.click_element(Order.order_button_at_the_top_of_the_page)

    def fill_name(self, name):
        self.find_element(Order.field_name).send_keys(name)

    def fill_last_name(self, last_name):
        self.find_element(Order.last_name_field).send_keys(last_name)

    def fill_address(self, address):
        self.find_element(Order.address_field).send_keys(address)

    def select_metro_station(self):
        self.click_element(Order.field_metro_station)
        self.click_element(Order.metro_station_1)

    def fill_phone(self, phone):
        self.find_element(Order.phone_field).send_keys(phone)

    def click_next_button(self):
        self.click_element(Order.next_button)

    def select_date(self):
        self.click_element(Order.field_when_to_bring_scooter)
        self.click_element(Order.date)

    def select_rental_period(self):
        self.click_element(Order.rental_period_field)
        self.click_element(Order.rental_period)

    def select_scooter_color(self):
        self.click_element(Order.scooter_color_field)
        self.click_element(Order.scooter_color_black)

    def fill_comment(self, comment):
        comment_field = self.find_element(Order.comment_field)
        comment_field.clear()
        comment_field.send_keys(comment)

    def click_order_button_final(self):
        self.click_element(Order.order_button)

    def confirm_order(self):
        self.click_element(Order.yes_button)