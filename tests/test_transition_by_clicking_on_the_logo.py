from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.pages_transition_by_clicking_on_the_logo import LogoPage
import urls


class TestLogoClicking:

    def test_order_button_and_scooter_logo_home_page_opens(self, browser):
        order_page = LogoPage(browser)

        order_page.click_order_button()

        order_page.click_scooter_logo()

        current_url = browser.current_url
        assert current_url == urls.base_url + urls.home_page, f"Expected URL to be '{urls.base_url + urls.home_page}', but got '{current_url}'"

    def test_yandex_logo_opens_in_new_tab_dzen_open(self, browser):
        logo_page = LogoPage(browser)

        initial_window = browser.current_window_handle

        logo_page.click_yandex_logo()

        WebDriverWait(browser, 5).until(expected_conditions.new_window_is_opened([initial_window]))

        new_window = [window for window in browser.window_handles if window != initial_window][0]
        browser.switch_to.window(new_window)

        WebDriverWait(browser, 10).until(expected_conditions.url_contains(urls.dzen))

        current_url = browser.current_url
        assert current_url == urls.dzen, f"Expected URL to be '{urls.dzen}', but got '{current_url}'"