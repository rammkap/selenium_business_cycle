import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.page_account import PageAccount
from pages.page_cart import Cart
from pages.page_checkout import Checkout
from pages.page_grappling import PageGrappling
from pages.page_main import PageMain
from pages.page_rashguards import PageRashguards
from product_cards.pc_LPI_preto import LPLpreto


def test_smoke_business_cycle(test_suite, test_case):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    login = PageMain(driver)
    login.perform_login() # performing authorization

    time.sleep(3) # added such a waiting since get 'StaleElementReferenceException', web-site is slow
    grappling = PageAccount(driver)
    grappling.go_to_grappling() # go to 'grappling' page

    rashguards = PageGrappling(driver)
    rashguards.go_to_rashguards() # go to 'rashguards' page

    time.sleep(5)  # added such a waiting since get 'StaleElementReferenceException', web-site is slow
    rashguard = PageRashguards(driver)
    rashguard.apply_filters() # first, we apply filters using one method so that Selenium can save the variables later
    rashguard_name = rashguard.get_product_LPI_preto_name().text
    rashguard_price = rashguard.get_product_LPI_preto_price1().text[:-1]
    rashguard_price_dot = float(rashguard_price.replace(',', '.'))
    rashguard.click_product_LPI_preto() # using a separate method, we go to the product card page

    choose_product = LPLpreto(driver) # first, we import the class to save the variables
    rashguard_name2 = choose_product.get_product_LPI_preto2().text
    rashguard_price2 = choose_product.get_product_LPI_preto_price2().text[:-1]
    rashguard_price2_dot = float(rashguard_price2.replace(',', '.'))
    assert  rashguard_name == rashguard_name2
    print('Name is the same')
    assert  rashguard_price_dot == rashguard_price2_dot
    print('Price is the same')
    choose_product.choose_and_go_to_cart() # now we use the method of going to the cart

    go_to_cart = Cart(driver)
    go_to_cart.go_to_checkout()

    pay = Checkout(driver) # first, we import the class to save the variables
    rashguard_name3 = pay.get_product_LPI_preto3().text
    rashguard_price3 = pay.get_product_LPI_preto_total_price().text[:-1] # I use indexes to trim the string '33.95$'
    rashguard_price3_dot = float(rashguard_price3.replace(',', '.'))
    envio_price = pay.get_price_envio().text[:-1]
    envio_price_dot = float(envio_price.replace(',', '.'))
    assert rashguard_name3 == rashguard_name3
    print('Name is the same')
    assert round(rashguard_price2_dot, 2) == round(rashguard_price3_dot - envio_price_dot, 2)
    print('Price is the same')
    pay.payment()

    driver.quit()


