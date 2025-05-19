from locators.faq import Faq
from pages.base_page import BasePage
from allure import step


class FaqPage(BasePage):

    @step("Прокрутка к разделу FAQ")
    def scroll_to_faq(self):
        self.scroll_into_view(Faq.faq_header_locator)

    @step("Клик по вопросу: {question_locator}")
    def click_question(self, question_locator):
        self.click_element(question_locator)

    @step("Получение текста ответа по локатору: {answer_locator}")
    def get_answer_text(self, answer_locator):
        return self.get_element_text(answer_locator)