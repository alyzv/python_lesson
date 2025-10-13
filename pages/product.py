from selenium.webdriver.common.by import By
import allure

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        with allure.step('Check produck title'):
            page_title = self.driver.find_element(By.CSS_SELECTOR,value='h2')
            assert page_title.text == title