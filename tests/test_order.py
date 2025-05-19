from pages.order_page import OrderPage
from data import name_1, name_2, last_name_1, last_name_2, address_1, address_2, phone_1, phone_2, comment


class TestOrder:

    def test_create_first_order_the_order_has_been_placed(self, browser):

        order_page = OrderPage(browser)

        order_page.click_order_button()

        order_page.fill_name(name_1)
        order_page.fill_last_name(last_name_1)
        order_page.fill_address(address_1)
        order_page.select_metro_station()
        order_page.fill_phone(phone_1)

        order_page.click_next_button()

        order_page.select_date()
        order_page.select_rental_period()
        order_page.select_scooter_color()
        order_page.fill_comment(comment)

        order_page.click_order_button_final()

        order_page.confirm_order()

        confirmation_message = order_page.get_confirmation_message()
        assert "Заказ оформлен" in confirmation_message

    def test_create_second_order_the_order_has_been_placed(self, browser):
        order_page = OrderPage(browser)

        order_page.scroll_to_bottom()
        order_page.click_order_button_in_middle()

        order_page.fill_name(name_2)
        order_page.fill_last_name(last_name_2)
        order_page.fill_address(address_2)
        order_page.select_metro_station()
        order_page.fill_phone(phone_2)

        order_page.click_next_button()

        order_page.select_date()
        order_page.select_rental_period()
        order_page.select_scooter_color()
        order_page.fill_comment(comment)

        order_page.click_order_button_final()

        order_page.confirm_order()

        confirmation_message = order_page.get_confirmation_message()
        assert "Заказ оформлен" in confirmation_message