import pytest
from HW_lesson18.TextBoxPage import TextBoxPage
from HW_lesson18.conftest import chrome


import time
class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Pavlo")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Pavlo"

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_field("sabina@gmail.com")
        page.scroll_down()
        page.click_submit()
        email_field = page.get_result_email()
        assert email_field.replace("Email:", "") == "sabina@gmail.com"

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_address_field("Louisville NY 40018-1234")
        page.scroll_down()
        page.click_submit()
        current_text_area_field = page.get_result_current_address()
        assert current_text_area_field.replace("Current Address :", "") == "Louisville NY 40018-1234"

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_address_field("Lvov, UA 56-10356")
        page.scroll_down()
        page.click_submit()
        permanent_text_area_field = page.get_result_permanent_address()
        assert permanent_text_area_field.replace("Permananet Address :", "") == "Lvov, UA 56-10356"

