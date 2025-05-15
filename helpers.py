from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def get_new_window_handle(browser, initial_window_handle, timeout=10):
    WebDriverWait(browser, timeout).until(
        expected_conditions.new_window_is_opened([initial_window_handle])
    )
    for handle in browser.window_handles:
        if handle != initial_window_handle:
            return handle
    raise Exception("New window handle not found")