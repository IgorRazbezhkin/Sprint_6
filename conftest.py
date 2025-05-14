import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")

    yield driver

    driver.quit()

@pytest.fixture
def manage_tabs(request, browser):
    initial_window = browser.current_window_handle

    def cleanup():
        all_windows = browser.window_handles

        for window in all_windows:
            if window != initial_window:
                browser.switch_to.window(window)
                browser.close()

        browser.switch_to.window(initial_window)

    request.addfinalizer(cleanup)
    return initial_window