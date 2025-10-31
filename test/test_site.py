from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProductPage
import allure

@allure.feature('Test homepage')
@allure.story('Title check')
def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    productpage = ProductPage(driver)
    productpage.check_title_is('Samsung galaxy s6')

@allure.feature('Test homepage')
@allure.story('Product count')
def test_two_items(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor() 
    homepage.check_products_count(2)