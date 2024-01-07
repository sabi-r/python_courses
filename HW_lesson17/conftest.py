import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="/Users/sabina/Desktop/Python/HW_lesson17/chromedriver")
    yield driver
    driver.quit()
