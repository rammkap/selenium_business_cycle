from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PageMain(Base):

    url = 'https://www.estilomma.pt/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Default data

    default_email = 'azrorus@gmail.com'
    default_password = 'selenium2025'

    # Locators

    button_reject = "//div[@class='cookie-consent__popup-button-reject']" # при открытии сайта открывается окно с куки
    button_main_login = "(//span[@data-mfp-src='#lgin'])[2]"
    field_email = "//input[@type='email']"
    field_password = "//input[@type='password']"
    button_login = "//input[@value='Log In']"

    # Getters

    def get_button_reject(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_reject))))

    def get_button_main_login(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_main_login))))

    def get_field_email(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.field_email))))

    def get_field_password(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.field_password))))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.button_login))))

    # Actions

    def click_button_reject(self):
        self.get_button_reject().click()
        print('Reject button clicked')

    def click_button_main_login(self):
        self.get_button_main_login().click()
        print('Main Login button clicked')

    def input_field_email(self, email):
        self.get_field_email().send_keys(email)
        print("Email entered")

    def input_field_password(self, password):
        self.get_field_password().send_keys(password)
        print("Password entered")

    def click_button_login(self):
        self.get_button_login().click()
        print("Login button clicked")

    # Methods

    def perform_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_reject()
        self.click_button_main_login()
        self.input_field_email(self.default_email)
        self.input_field_password(self.default_password)
        self.click_button_login()