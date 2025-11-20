import datetime
import time


class Base():

    def __init__(self, driver):
        self.driver = driver

    # Method - get current URL

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL is {get_url}')


    # Method - make screenshot

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(
            'C:\\Users\\screenshots\\' + name_screenshot)