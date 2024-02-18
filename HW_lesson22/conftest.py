import pytest
import requests


@pytest.fixture(scope="class")
def exchange_rates_fixture(request):
    response = requests.request(method="GET", url="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    if response.status_code == 200:
        return response.json()
    else:
        return None
