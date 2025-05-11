import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.pages_faq import FaqPage
from locators.faq import Faq


@pytest.mark.parametrize("question_locator,text_locator", [
    (Faq.heading_0, Faq.text_heading_0),
    (Faq.heading_1, Faq.text_heading_1),
    (Faq.heading_2, Faq.text_heading_2),
    (Faq.heading_3, Faq.text_heading_3),
    (Faq.heading_4, Faq.text_heading_4),
    (Faq.heading_5, Faq.text_heading_5),
    (Faq.heading_6, Faq.text_heading_6),
    (Faq.heading_7, Faq.text_heading_7),
])
def test_faq_questions(browser, question_locator, text_locator):
    faq_page = FaqPage(browser)

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(Faq.table_of_contents_text))

    faq_page.scroll_to_faq()

    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(question_locator))

    faq_page.click_question(question_locator)

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(text_locator))

    answer_text = faq_page.get_answer_text(text_locator)

    assert answer_text != "", f"Ответ на вопрос {question_locator} не найден."