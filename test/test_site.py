from selenium.webdriver.common.by import By
import time #bad example
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    productpage = ProductPage(driver)
    productpage.check_title_is('Samsung galaxy s6')

def test_two_items(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2) # bad example
    homepage.check_products_count(2)