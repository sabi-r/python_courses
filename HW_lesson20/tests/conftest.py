import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="/Users/sabina/Desktop/Python/HW_lesson20/chrome_driver")
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def firefox(request):
    driver = webdriver.Firefox(executable_path="/Users/sabina/Desktop/Python/HW_lesson20/geckodriver")
    request.cls.driver = driver
    driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome(executable_path="/Users/sabina/Desktop/Python/HW_lesson20/chrome_driver")
    request.cls.driver = driver
    yield driver
    driver.quit()
