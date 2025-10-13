from selenium.webdriver.common.by import By
import allure

class HomePage:
    def __init__(self, driver):
         self.driver = driver

    def open(self):
        with allure.step('Open Home page'):
            self.driver.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self):
        with allure.step('Find element Samsung Galaxy s6'):
            galaxy_s6 = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
            galaxy_s6.click()

    def click_monitor(self):
        with allure.step('Click on element Samsung Galaxy s6'):
            monitor_link = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
            monitor_link.click()

    def check_products_count(self, count):
        with allure.step('Check products count'):
            monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
            assert len(monitors) == count