# 3) Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.
#  до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого).
#  Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення в файл
# коли ми запустили тест та текстове повідомлення що ми стартанули.
# Тердаун буде писати повідомлення що ми закінчили і також час коли закінчили використайте вже відому
# вам бібліотеку дататайм

import pytest
from datetime import datetime
from lesson_15 import Calculator

class TestCalculator:
    @classmethod
    def setup_class(cls):
        cls.setup_time = datetime.now()
        with open("test_log.txt", "a") as file:
            file.write(f"Тест стартував: {cls.setup_time}\n")
        Calculator.greeting_message()

    @classmethod
    def teardown_class(cls):
        teardown_time = datetime.now()
        with open("test_log.txt", "a") as file:
            file.write(f"Тест закінчився: {teardown_time}\n")
            file.write(f"Тривалість тесту: {teardown_time - cls.setup_time}\n")

    @pytest.fixture
    def calculator_instance(self):
        return Calculator()

    @pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (0, 0, 0), (-1, 1, 0), (10, -5, 5), (-8, -2, -10)])
    def test_addition(self, calculator_instance, a, b, expected):
        result = calculator_instance.addition(a, b)
        assert result == expected

    @pytest.mark.parametrize("a, b, expected", [(6, 3, 2), (10, 2, 5), (-25, -5, 5), (0, 5, 0), (25, 5, 5)])
    def test_division(self, calculator_instance, a, b, expected):
        result = calculator_instance.division(a, b)
        assert result == expected
