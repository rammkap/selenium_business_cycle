import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from logs.logger import Logger


class PageRashguards(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_filter = "//span[contains(text(), 'Filtros')]"
    filter_sizes = "//div[contains(text(), 'Tamanhos')]"
    checkbox_L = "//label[@for='tll_14']"
    filter_order = "(//div[@class='xaccordion-title'])[4]"
    checkbox_price = "//label[@for='st_5']"
    product_LPI_preto = "//img[@title='Rashguard de manga curta Leone Primal Instinct - preto']"
    product_LPI_preto_name = "//h2[@title='Rashguard de manga curta Leone Primal Instinct - preto']"
    product_LPI_preto_price1 = "//*[@id='scrollingcontent']/div/div/div[3]/a/div[2]"

    # Getters

    def get_button_filter(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_filter))))

    def get_filter_sizes(self):
        return WebDriverWait(self.driver, 60).until((EC.visibility_of_element_located((By.XPATH, self.filter_sizes))))

    def get_checkbox_L(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located((By.XPATH, self.checkbox_L))))

    def get_filter_order(self):
        return WebDriverWait(self.driver, 60).until((EC.visibility_of_element_located((By.XPATH, self.filter_order))))

    def get_checkbox_price(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located((By.XPATH, self.checkbox_price))))

    def get_product_LPI_preto(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.product_LPI_preto))))

    def get_product_LPI_preto_name(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located((By.XPATH, self.product_LPI_preto_name))))

    def get_product_LPI_preto_price1(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located((By.XPATH, self.product_LPI_preto_price1))))

    # Actions

    def click_button_filter(self):
        self.get_button_filter().click()
        print('Filter clicked')

    def click_filter_sizes(self):
        self.get_filter_sizes().click()
        print('Filter sizes clicked')

    def click_checkbox_L(self):
        self.get_checkbox_L().click()
        print('Checkbox "L" clicked')

    def click_filter_order(self):
        self.get_filter_order().click()
        print('Filter order clicked')

    def click_checkbox_price(self):
        self.get_checkbox_price().click()
        print('Checkbox "By price" clicked')

    def click_product_LPI_preto(self):
        self.get_product_LPI_preto().click()
        print('LPI preto has chosen')

    # Methods

    def apply_filters(self):
        Logger.add_start_step(method='apply_filters')
        self.click_button_filter()
        time.sleep(10)
        self.click_filter_sizes()
        self.click_checkbox_L()
        time.sleep(5)
        self.click_button_filter()
        self.click_filter_order()
        self.click_checkbox_price()
        Logger.add_end_step(url=self.driver.current_url, method='apply_filters')