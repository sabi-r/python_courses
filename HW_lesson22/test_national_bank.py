import pytest
from datetime import datetime

@pytest.mark.usefixtures("exchange_rates_fixture")
class TestExchangeRates:

    def test_exchange_rates_file_creation(self, exchange_rates_fixture):
        exchange_rates_data = exchange_rates_fixture
        if exchange_rates_data:
            exchange_rates_str = f"[Дата запита]: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            for i, item in enumerate(exchange_rates_data, 1):
                exchange_rates_str += f"{i}. {item['txt']} до гривні: {item['rate']}\n"

            with open("info_nbu.txt", "w") as file:
                file.write(exchange_rates_str)
            assert True
        else:
            assert False, "Не вдалося получити данні про курси валют з API."