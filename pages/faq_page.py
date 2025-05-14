from locators.faq import Faq
from pages.base_page import BasePage


class FaqPage(BasePage):

    def scroll_to_faq(self):
        self.scroll_into_view(Faq.faq_header_locator)

    def click_question(self, question_locator):
        self.click_element(question_locator)

    def get_answer_text(self, answer_locator):
        return self.get_element_text(answer_locator)