from locators.order import Order
from locators.transition_by_clicking_on_the_logo import Logo
from pages.base_page import BasePage
from allure import step


class LogoPage(BasePage):

    @step("Кликнуть по кнопке 'Заказать' вверху страницы")
    def click_order_button(self):
        self.click_element(Order.order_button_at_the_top_of_the_page)

    @step("Кликнуть по логотипу самоката")
    def click_scooter_logo(self):
        self.click_element(Logo.logo_scooter)

    @step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(Logo.yandex_logo)