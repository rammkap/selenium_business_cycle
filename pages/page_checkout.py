import time

from selenium.webdriver import Keys
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

    # Getters

    def get_button_payment(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_payment))))

    # Actions

    def click_button_payment(self):
        self.get_button_payment().click()
        print('Payment button clicked')

    # Methods

    def payment(self):
        self.click_button_payment()
        self.get_screenshot()