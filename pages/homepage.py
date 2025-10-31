from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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
            print("IS Clicked")

    def check_products_count(self, count):
        with allure.step('Check products count'):
            wait = WebDriverWait(self.driver, 5)
            element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".card"), "Apple monitor 24"))
            monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
            print(monitors)
            assert len(monitors) == count