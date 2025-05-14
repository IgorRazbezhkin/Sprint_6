from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.transition_by_clicking_on_the_logo import Logo


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_yandex_logo(self):
        wait = WebDriverWait(self.driver, 5)
        yandex_logo = wait.until(expected_conditions.element_to_be_clickable(Logo.yandex_logo))
        yandex_logo.click()

    def wait_for_new_window(self, initial_window_handle, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.new_window_is_opened([initial_window_handle])
        )

    def wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(expected_url)
        )