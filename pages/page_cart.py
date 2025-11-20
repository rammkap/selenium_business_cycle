from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_final = "//span[@class='bton-dflt rlzp obf']"

    # Getters

    def get_button_final(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_final))))

    # Actions

    def click_button_filter(self):
        self.get_button_final().click()
        print('Final button clicked')

    # Methods

    def go_to_checkout(self):
        self.click_button_filter()