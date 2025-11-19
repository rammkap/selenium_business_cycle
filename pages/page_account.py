import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class PageAccount(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    tab_grappling = "//a[@title='Grappling']"

    # Getters

    def get_tab_grappling(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.tab_grappling))))

    # Actions

    def click_tab_grappling(self):
        self.get_tab_grappling().click()
        print('Grappling tab clicked')


    # Methods

    def go_to_grappling(self):
        self.click_tab_grappling()



