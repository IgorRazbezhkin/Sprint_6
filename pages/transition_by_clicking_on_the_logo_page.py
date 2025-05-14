from locators.order import Order
from locators.transition_by_clicking_on_the_logo import Logo
from pages.base_page import BasePage


class LogoPage(BasePage):

    def click_order_button(self):
        self.click_element(Order.order_button_at_the_top_of_the_page)

    def click_scooter_logo(self):
        self.click_element(Logo.logo_scooter)