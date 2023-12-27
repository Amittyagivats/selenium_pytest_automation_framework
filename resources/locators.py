from selenium.webdriver.common.by import By
from resources.elements import PageElements


class PageLocators():
    SEARCH_STOCKS = (By.XPATH, PageElements.SEARCH_FIELD)
    