# import pytest
# from HW_lesson9 import add_three_numbers


# solution 1
# def test_1():
#     assert add_three_numbers(3, 4, 3) == 10


# solution 2
# @pytest.mark.parametrize("numb_1, numb_2, numb_3, result", [
#     pytest.param(3, 4, 3, 10, id="three positive"),
#     pytest.param(-3, 3, 3, 3, id="negative and 2 positive"),
#     pytest.param(-3, -1, -1, -5, id="three negative")])
# def test_set_1(numb_1, numb_2, numb_3, result):
#     assert add_three_numbers(numb_1, numb_2, numb_3) == result


# solution 3
# list_test = [(3, 4, 3, 10), (-3, 3, 3, 3), (-3, -1, -1, -5)]


# @pytest.mark.parametrize("numb_1, numb_2, numb_3, result", list_test)
# def test_set_2(numb_1, numb_2, numb_3, result):
#     assert add_three_numbers(numb_1, numb_2, numb_3) == result
