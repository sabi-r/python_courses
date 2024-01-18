import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def chrome():
    driver = webdriver.Chrome(executable_path="/Users/sabina/Desktop/Python/HW_lesson19/chromedriver")
    yield driver
    driver.quit()
