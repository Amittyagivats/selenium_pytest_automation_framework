import pytest
import logging
from softest import TestCase
from selenium.webdriver.common.by import By
# from   import soft_assert, verify_expectations
from pages.home_page import HomePage
import pdb

log = logging.getLogger()

def factorial_function(number):
   # Perform a check whether the input number is positive or not, if it is not
   # positive, raise an assert
    assert number >= 0. and type(number) is int, "The input is not recognized"
 
    if number == 0:
        return 1
    else:
      # recursive function to calculate factorial
        return number * factorial_function(number - 1)

# def resource_1_setup():
#     print('Setup for resource 1 called')

# def resource_1_teardown():
#     print('Teardown for resource 1 called')
    
# class AssertionTest(softest.TestCase):
#     resource_1_setup()
#     resource_1_teardown()

def test_mock(monkeypatch):
    # result = HomePage.multiply1(2,3)
    # assert result == 6
    
    def mock_fun(x,y):
        return x+y
    
    monkeypatch.setattr(HomePage, "multiply1", mock_fun)
    
    result = HomePage.multiply1(2,3)
    assert result == 5
    
        
    

    
@pytest.mark.xfail
@pytest.mark.parametrize("value1,value2,expected",[(10,20,3)])
def test_home_page_loads(value1,value2,expected):
    # pdb.set_trace()
    expected = value1 + value2
    # pytest.skip("result==30")
    assert expected < 10, "Value2 is not less than the result"
    # pytest.skip("expected==30")
    # assert factorial_function(4)==30, "Not Equal"


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(6, 0)








    

#     # Assert
#     # try:
#     # TestCase.soft_assert(TestCase.assertEqual, result, 30, "Not Equal")
#     # self.soft_assert(self.assertEqual, value1, result, "Not Less")
#     # self.soft_assert(self.assertGreater, value1, result, "Not Greater")
    
#     # TestCase.assert_all("Verify result")
#     # TestCase.soft_assert(value1 < result, "Value1 is not less than the result"
    # assert value2 < result, "Value2 is not less than the result"
#     # except AssertionError as e:
#     #     pytest.fail(f"Assertion failed: {e}")
    
#     # home_page = HomePage(browser)
#     # home_page.open("/")
#     # check.equal(factorial_function(4),23)
#     # check.equal(factorial_function(0),1)
#     # check.equal(home_page.is_page_loaded(),True)
#     # assert ("Google Finance - Stock Market Prices, Real-time Quotes & Business News"
#     #     == home_page.get_page_title())
    
    
    
#     # destinationFileName = r"test_snapshot.png"
#     # browser.save_screenshot(destinationFileName)
#     # log.info("Web Page is loaded successfully.")
#     # verify_expectations()
# @pytest.mark.run(order=2)
# @pytest.mark.smoke_suite
# def test_verify_page_title(browser):
#     home_page = HomePage(browser)
#     home_page.open("/")
    
#     assert (
#         "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
#         == home_page.get_page_title()
#     )

# @pytest.mark.smoke_suite
# def test_search_stock(browser):
#     home_page = HomePage(browser)
#     home_page.open("/")
#     home_page.search_stock("R Systems International Ltd")
#     web_element = browser.find_element(By.XPATH, "//div[@class='zzDege']")
#     assert "R Systems International Ltd" in web_element.text
    # @pytest.mark.run(order=1)
    # @pytest.mark.smoke_suite
    # def test_news_section(browser):
    #     home_page = HomePage(browser)
    #     home_page.open("/")
    #     assert home_page.is_news_section_visible()

# def test_market_summary(browser):
#     home_page = HomePage(browser)
#     home_page.open("/")
#     webText = home_page.is_market_summary_available()
#     assert "Explore market trends" in webText

# def test_portfolio_management_visibility(browser):
#     home_page = HomePage(browser)
#     home_page.open("/")
#     webText = home_page.portfolio_management_section_present()
#     assert "Portfolios" in webText

# def test_currency_exchange_visibility(browser):
#     home_page = HomePage(browser)
#     home_page.open("/")
#     assert home_page.is_currency_exchange_visible()   

# def test_watchlist_section_availability(browser):
#     home_page = HomePage(browser)
#     home_page.open("/")
#     watchlist_available = home_page.is_watchlist_available()
#     assert 'Watchlist' in watchlist_available, "Watchlist section is not available"

# @pytest.mark.smoke_suite
# def test_settings_section_availability(browser):
#     home_page = HomePage(browser)
#     home_page.open("/")
#     webText = home_page.settings_present()
#     assert "Settings" in webText
      
# def test_send_feedback_section_availability(browser):
#     home_page = HomePage(browser)
#     home_page.open("/")
#     webText = home_page.feedback_present()
#     assert "Send feedback" in webText
   
# def test_most_active_section_availability(browser):
#     home_page = HomePage(browser)
#     home_page.open("/")
#     webText = home_page.active_section_present()
#     assert "Most Active" in webText