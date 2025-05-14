from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.pages_transition_by_clicking_on_the_logo import LogoPage


class TestLogoClicking:

    def test_order_button_and_scooter_logo_home_page_opens(self, browser):
        order_page = LogoPage(browser)

        order_page.click_order_button()

        order_page.click_scooter_logo()

        current_url = browser.current_url
        assert current_url == "https://qa-scooter.praktikum-services.ru/", f"Expected URL to be 'https://qa-scooter.praktikum-services.ru/', but got '{current_url}'"

    def test_yandex_logo_opens_in_new_tab_dzen_open(self, browser):
        logo_page = LogoPage(browser)

        initial_window = browser.current_window_handle

        logo_page.click_yandex_logo()

        WebDriverWait(browser, 5).until(expected_conditions.new_window_is_opened([initial_window]))

        new_window = [window for window in browser.window_handles if window != initial_window][0]
        browser.switch_to.window(new_window)

        WebDriverWait(browser, 10).until(expected_conditions.url_contains("https://dzen.ru/?yredirect=true"))

        current_url = browser.current_url
        assert current_url == "https://dzen.ru/?yredirect=true", f"Expected URL to be 'https://dzen.ru/?yredirect=true', but got '{current_url}'"