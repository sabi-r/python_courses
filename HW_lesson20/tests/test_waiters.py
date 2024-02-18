import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("chrome_class")
class TestWaiters:

    def test_connection(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        visible_invisible_button_loc = (By.CSS_SELECTOR, "#visibleAfter")  # = (By.ID, "visibleAfter")
        ##explicity wait start##
        WebDriverWait(self.driver, timeout=5).until(ec.visibility_of_element_located(visible_invisible_button_loc))
        visible_invisible_button = self.driver.find_element(*visible_invisible_button_loc)
        ##explicity wait end##
        visible_invisible_button.click()
        assert visible_invisible_button.is_enabled()  # мені не підтянуло чомусь ніякі нативні методи для цієї кнопки,
                                                      # я руками дописала і тест пройшов.

    def test_connection_enable(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        disable_enable_button_loc = (By.ID, "enableAfter")
        disable_enable_button: WebElement = self.driver.find_element(*disable_enable_button_loc)
        WebDriverWait(self.driver, 10).until(
            ec.text_to_be_present_in_element_attribute(disable_enable_button_loc, "class", "btn-primary")
        )
        disable_enable_button.click()
        assert disable_enable_button.is_displayed()


    def test_connection_color(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        colored_button_loc = (By.ID, "colorChange")
        colored_button: WebElement = self.driver.find_element(*colored_button_loc)@
        WebDriverWait(self.driver, 5).until(
            ec.text_to_be_present_in_element_attribute(colored_button_loc, "class", "text-danger"))
        colored_button.click()
        assert colored_button.is_enabled()
