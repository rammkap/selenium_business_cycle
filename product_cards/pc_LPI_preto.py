from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class LPLpreto(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_size_L = "//li[@data-option='14']"
    button_add_to_cart = "(//button[@class='bton-buy-stock bton-buy buy-popup'])[1]"
    button_go_to_cart = "//a[@class='shw-crt']"
    product_LPI_preto2 = "//h1[@class='title']"
    product_LPI_preto_price2 = "//span[@id='price-container']"

    # Getters

    def get_button_size_L(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_size_L))))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart))))

    def get_button_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_go_to_cart))))

    def get_product_LPI_preto2(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located((By.XPATH, self.product_LPI_preto2))))

    def get_product_LPI_preto_price2(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located((By.XPATH, self.product_LPI_preto_price2))))

    # Actions

    def click_button_size_L(self):
        self.get_button_size_L().click()
        print('Size "L" clicked')

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print('Add to cart clicked')

    def click_button_go_to_cart(self):
        self.get_button_go_to_cart().click()
        print('Go to cart clicked')

    # Methods

    def choose_and_go_to_cart(self):
        self.click_button_size_L()
        self.click_button_add_to_cart()
        self.click_button_go_to_cart()



