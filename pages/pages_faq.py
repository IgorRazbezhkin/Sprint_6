from locators.faq import Faq


class FaqPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_faq(self):
        faq_header_element = self.driver.find_element(*Faq.faq_header_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_header_element)

    def click_question(self, question_locator):
        question_element = self.driver.find_element(*question_locator)
        question_element.click()

    def get_answer_text(self, answer_locator):
        return self.driver.find_element(*answer_locator).text