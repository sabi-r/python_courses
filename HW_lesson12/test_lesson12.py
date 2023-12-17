import requests
import pytest


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    # перевірити поля "icon_url" чи він не пусти + чи це картинка,  - 2 теста
    def test_check_icon(self):
        icon_url = self.response.json().get("icon_url")
        assert icon_url is not None, "Icon URL is missing in the response"
        assert icon_url[-4:].lower() == ".png", "The image URL does not end with '.png'"

    # перевірити чи є ключ "value"  і перевірити його значення - 2 теста
    def test_check_key_value(self):
        assert "value" in self.response.json(), "Key 'value' is missing in the response"


    def test_check_value_key_value(self):
        value = self.response.json().get("value")
        assert value is not None, "Value is missing in the response"

# ___________________________________________________________________________________________________________
# Зробити окремий клас
# пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# зробити класу фікстуру
# тест на статус код
# тест на кількість жартів
# тест на сам жарт
# + 3 тести

@pytest.mark.usefixtures("chucknorris_search_fixture")
class TestSearchQuery:
    def test_status_code(self):
        assert self.search_status_code == 200, "Invalid status code"

    def test_number_of_jokes(self):
        jokes_count = len(self.search_response.json()["result"])
        assert jokes_count == 0, "Not corresponding number of jokes"

    def test_verify_joke_existence(self):
        jokes = self.search_response.json()["result"]
        for joke in jokes:
            assert joke.get("joke"), "Empty or missing joke field"
