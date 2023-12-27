from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from resources.locators import PageLocators


class HomePage(BasePage):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.wait = WebDriverWait(browser, timeout=10)

    
    def multiply1(x, y):
        return x*y
    
    def is_page_loaded(self):
        try:
            self.wait.until(EC.presence_of_element_located(PageLocators.SEARCH_STOCKS))
            return True
        except Exception as e:
            print(f"Caught an unexpected exception: {e}")
            return False

    def get_page_title(self):
        return self.browser.title

    def search_stock(self, symbol):
        search_box = search_box()
        search_box.send_keys(symbol)
        search_box.send_keys(Keys.ENTER)

    def is_news_section_visible(self):
        news_section = self.browser.find_element(By.ID, "news-title")
        return news_section.is_displayed()

    def is_market_summary_available(self):
        try:
            tab_button = self.browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > svg")
            tab_button.click()
            market_summary_button = self.browser.find_element(
                By.XPATH, "//div[@class='jjm4k' and text()='Market trends']"
            )
            market_summary_button.click()

            market_summary = self.browser.find_element(
                By.XPATH, "//div[@class='TnyjJd']"
            )
            return market_summary.text
        except NoSuchElementException:
            return False
        
    def portfolio_management_section_present(self):
        
        tab_button = self.browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > svg")
        tab_button.click()
        wait = WebDriverWait(self.browser, 10)
        portfolio_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.s9af4d > div.HMVX2b > div:nth-child(4) > div")))
        element_text = self.browser.execute_script("return arguments[0].textContent;", portfolio_element)
        return element_text
    
    def is_currency_exchange_visible(self):
        try:
            currency_exchange_link = self.browser.find_element(By.XPATH,"(//*[@class='AHyjFe QwFhgb'])[1]")
            return currency_exchange_link.is_displayed()
        except Exception:
            return False
    
    def is_watchlist_available(self):
        
        tab_button = self.browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > svg")
        tab_button.click()
        wait = WebDriverWait(self.browser, 10)
        watchlist_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.s9af4d > div.HMVX2b > div:nth-child(5) > div")))
        element_text = self.browser.execute_script("return arguments[0].textContent;", watchlist_element)
        return element_text
    
    def settings_present(self):
        
        tab_button = self.browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > svg")
        tab_button.click()
        wait = WebDriverWait(self.browser, 10)
        settings_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Settings']")))
        element_text = self.browser.execute_script("return arguments[0].textContent;", settings_element)
        return element_text
    
    def feedback_present(self):
        
        tab_button = self.browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > svg")
        tab_button.click()
        wait = WebDriverWait(self.browser, 10)
        feedback_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Send feedback']")))
        element_text = self.browser.execute_script("return arguments[0].textContent;", feedback_element)
        return element_text
    
    def active_section_present(self):
        
        tab_button = self.browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > svg")
        tab_button.click()
        wait = WebDriverWait(self.browser, 10)
        most_active_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Most Active']")))
        element_text = self.browser.execute_script("return arguments[0].textContent;", most_active_element)
        return element_text