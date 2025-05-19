from selenium.webdriver.common.by import By


class Faq:
    table_of_contents_text = (By.XPATH, ".//div[@class='Home_Header__iJKdX' and contains(text(), 'Самокат')]")
    faq_header_locator = (By.XPATH, ".//div[@class='Home_SubHeader__zwi_E' and text()='Вопросы о важном']")
    heading_0 = (By.XPATH, ".//div[@id='accordion__heading-0']")
    text_heading_0 = (By.XPATH, ".//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    heading_1 = (By.XPATH, ".//div[@id='accordion__heading-1']")
    text_heading_1 = (By.XPATH, ".//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    heading_2 = (By.XPATH, ".//div[@id='accordion__heading-2']")
    text_heading_2 = (By.XPATH, ".//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    heading_3 = (By.XPATH, ".//div[@id='accordion__heading-3']")
    text_heading_3 = (By.XPATH, ".//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    heading_4 = (By.XPATH, ".//div[@id='accordion__heading-4']")
    text_heading_4 = (By.XPATH, ".//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    heading_5 = (By.XPATH, ".//div[@id='accordion__heading-5']")
    text_heading_5 = (By.XPATH, ".//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    heading_6 = (By.XPATH, ".//div[@id='accordion__heading-6']")
    text_heading_6 = (By.XPATH, ".//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    heading_7 = (By.XPATH, ".//div[@id='accordion__heading-7']")
    text_heading_7 = (By.XPATH, ".//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")