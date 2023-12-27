from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://finance.google.com"        

# def __init__(self, browser, app_url):
#     self.browser = browser
#     self.base_url = app_url


    def open(self, url):
        self.browser.maximize_window()  
        self.browser.get(self.base_url + url)
        self.browser.set_page_load_timeout(30)
        self.browser.implicitly_wait(5)

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            # WebDriverWait(self.driver, 10).until(EC.new_window_is_opened()
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()
