import pytest
import requests


@pytest.fixture(scope="class")
def fixture_random(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/random")
    request.cls.response = response
    yield response

@pytest.fixture(scope="class")
def chucknorris_search_fixture(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/search?query={query}")
    status_code = response.status_code
    request.cls.search_response = response
    request.cls.search_status_code = status_code
    yield response, status_code