from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.order import Order
from locators.transition_by_clicking_on_the_logo import Logo

class LogoPage:
    def __init__(self, browser):
        self.browser = browser

    def click_order_button(self):
        order_button = WebDriverWait(self.browser, 5).until(
            expected_conditions.element_to_be_clickable(Order.order_button_at_the_top_of_the_page)
        )
        order_button.click()

    def click_scooter_logo(self):
        scooter_logo = WebDriverWait(self.browser, 5).until(
            expected_conditions.element_to_be_clickable(Logo.logo_scooter)  # Замените на правильный селектор
        )
        scooter_logo.click()

    def click_yandex_logo(self):
        yandex_logo = WebDriverWait(self.browser, 5).until(
            expected_conditions.element_to_be_clickable(Logo.yandex_logo)  # Замените на правильный селектор
        )
        yandex_logo.click()