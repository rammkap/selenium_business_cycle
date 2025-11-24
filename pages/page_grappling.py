from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from logs.logger import Logger


class PageGrappling(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_rashguards = "(//a[@title='Rashguards'])[9]"

    # Getters

    def get_button_rashguards(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_rashguards))))

    # Actions

    def click_button_rashguards(self):
        self.get_button_rashguards().click()
        print('Rashguards section clicked')

    # Methods

    def go_to_rashguards(self):
        Logger.add_start_step(method='go_to_rashguards')
        self.click_button_rashguards()
        Logger.add_end_step(url=self.driver.current_url, method='go_to_rashguards')