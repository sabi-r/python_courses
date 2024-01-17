from selenium.webdriver.remote.webelement import WebElement

from HW_lesson19.DynamicPropertiesPage import PageDynamicProperties
from HW_lesson19.ElementsPage import ElementsPage
from HW_lesson19.conftest import chrome
import pytest


@pytest.mark.usefixtures("chrome")
class TestElementsPage:
    # def test_page(self, chrome):
    #     page = ElementsPage(chrome)
    #     page.open()
    #     elements = page.get_elements_page_categories()
    #     assert len(elements) == 33

    #  todo перевірити відповіді всіх 33 елементів в елементс
    #  assert elements[2] == "Radio Button"

    @pytest.mark.parametrize("expected_elements", [
        'Text Box',
        'Check Box',
        'Radio Button',
        'Web Tables',
        'Buttons',
        'Links',
        'Broken Links - Images',
        'Upload and Download',
        'Dynamic Properties',
        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    ])
    def test_element_verification(self, chrome, expected_elements):
        page = ElementsPage(chrome)
        page.open()
        actual_elements = page.get_elements_page_categories()
        for i,j in zip(actual_elements, expected_elements):
            assert i == j



    # def test_is_button_enabled(self, chrome):
    #     page = PageDynamicProperties(chrome)
    #     page.open()
    #     button: WebElement = page.disable_enable_button()
    #     button.click()
    #
    # def test_is_button_shown(self, chrome):
    #     page = PageDynamicProperties(chrome).open()  # короткий запис
    #     button: WebElement = page.button_invisible_visible()
    #     button.click()
