import pytest
import logging
from softest import TestCase
from selenium.webdriver.common.by import By
# from   import soft_assert, verify_expectations
from pages.home_page import HomePage
import pdb

log = logging.getLogger()

# @pytest.mark.run(order=2)
@pytest.mark.smoke_suite
def test_verify_page_title(browser):
    home_page = HomePage(browser)
    home_page.open("/")
    
    assert (
        "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
        == home_page.get_page_title()
    )

@pytest.mark.smoke_suite
def test_settings_section_availability(browser):
    home_page = HomePage(browser)
    home_page.open("/")
    webText = home_page.settings_present()
    assert "Settings" in webText
