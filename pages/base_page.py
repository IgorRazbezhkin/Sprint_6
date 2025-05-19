from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from allure import step


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    @step("Кликнуть по элементу {locator}")
    def click_element(self, locator):
        element = self.find_element(locator)
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    @step("Получить текст элемента {locator}")
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @step("Прокрутить к элементу {locator}")
    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @step("Прокрутить страницу до кнопки 'заказать' в середине страницы")
    def scroll_to_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @step("Ожидание открытия нового окна и переключения на него")
    def wait_for_new_window(self, initial_window_handle):
        self.wait.until(
            expected_conditions.new_window_is_opened([initial_window_handle])
        )
        for handle in self.driver.window_handles:
            if handle != initial_window_handle:
                self.driver.switch_to.window(handle)
                return handle
        raise Exception("New window handle not found")

    @step("Получить текущий handle окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @step("Ожидание URL: {expected_url}")
    def wait_for_url(self, expected_url):
        self.wait.until(
            expected_conditions.url_to_be(expected_url)
        )

    @step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url