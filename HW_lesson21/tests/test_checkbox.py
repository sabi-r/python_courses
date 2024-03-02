import pytest
from HW_lesson21.CheckboxPage import CheckboxPage

@pytest.mark.usefixtures("firefox")
class TestCheckboxPage:
    def setup_method(self):
        self.page = CheckboxPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.expand_folder("home")
        self.page.mark_folder("home")
        self.page.collapse_folder("home")
        self.page.unmark_folder("home")
        pass