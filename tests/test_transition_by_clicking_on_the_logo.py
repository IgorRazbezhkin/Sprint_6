from pages.transition_by_clicking_on_the_logo_page import LogoPage
import urls


class TestLogoClicking:

    def test_order_button_and_scooter_logo_home_page_opens(self, browser):
        order_page = LogoPage(browser)

        order_page.click_order_button()

        order_page.click_scooter_logo()

        current_url = order_page.get_current_url()
        assert current_url == urls.base_url + urls.home_page, f"Expected URL to be '{urls.base_url + urls.home_page}', but got '{current_url}'"

    def test_yandex_logo_opens_in_new_tab_dzen_open(self, browser):
        logo_page = LogoPage(browser)

        logo_page.click_yandex_logo()

        initial_window = logo_page.get_current_window_handle()
        logo_page.wait_for_new_window(initial_window)

        logo_page.wait_for_url(urls.dzen)

        current_url = logo_page.get_current_url()
        assert current_url == urls.dzen, f"Expected URL to be '{urls.dzen}', but got '{current_url}'"