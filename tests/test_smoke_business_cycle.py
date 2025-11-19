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
    login.perform_login()
    time.sleep(3) # добавил такое ожидание так как иначе получаю ошибку StaleElementReferenceException
    grappling = PageAccount(driver)
    grappling.go_to_grappling()
    rashguards = PageGrappling(driver)
    rashguards.go_to_rashguards()
    time.sleep(5)  # добавил такое ожидание так как иначе получаю ошибку StaleElementReferenceException
    rashguard = PageRashguards(driver)
    rashguard.find_LPI_preto()
    choose_product = LPLpreto(driver)
    choose_product.choose_and_go_to_cart()
    go_to_cart = Cart(driver)
    go_to_cart.go_to_checkout()
    pay = Checkout(driver)
    pay.payment()


