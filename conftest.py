import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specify the browser (chrome/firefox)"
    )


# @pytest.fixture(params=["chrome", "firefox"], scope="class")
@pytest.fixture
def browser(request):
    
    browser_name = request.config.getoption("--browser")
    
    if browser_name == 'chrome':
        chrome_service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(service=chrome_service,options=options)
    elif browser_name == 'firefox':
        options = Options() 
        options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options)
        
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    
    yield driver
    driver.quit()



# Fixture for application URL
# @pytest.fixture
# def app_url():
#     return "https://example.com"

# Fixture for a configuration setting
@pytest.fixture
def some_config():
    return "some_config_value"

# Test-level fixture (autouse makes it apply to all tests automatically)
@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup code that runs before each test
    print("Setting up before test")

    yield  # This is where the test will run

    # Teardown code that runs after each test
    print("Tearing down after test")