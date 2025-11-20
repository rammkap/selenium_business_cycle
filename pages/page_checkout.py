from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Checkout(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_payment = "//a[@id='confirmar_pedido']"
    product_LPI_preto3 = "//td[@class='main' and contains(., 'Rashguard de manga curta Leone Primal Instinct')]"
    product_LPI_preto_total_price = "//strong[@id='price-scalapay']"
    price_envio = "//tr[@data-total='ot_shipping']/td[2]"

    # Getters

    def get_button_payment(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_payment))))

    def get_product_LPI_preto3(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located((By.XPATH, self.product_LPI_preto3))))

    def get_product_LPI_preto_total_price(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located((By.XPATH, self.product_LPI_preto_total_price))))

    def get_price_envio(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located((By.XPATH, self.price_envio))))

    # Actions

    def click_button_payment(self):
        self.get_button_payment().click()
        print('Payment button clicked')

    # Methods

    def payment(self):
        self.click_button_payment()
        self.get_screenshot()