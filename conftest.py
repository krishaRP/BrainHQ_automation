import pytest
from selenium import webdriver

# create a pytest fixture for pytest
@pytest.fixture
def driver():
    url = "https://www.brainhq.com"
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.close()