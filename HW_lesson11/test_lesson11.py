# 2) Напишіть 5 тестів з затримкою в 2 секунди кожен, один з тестів повинен мати унікальне імя.
#  Запустіть їх за домогою pytest-xdist ліби в 5 потоків.
#  Запустіть цей ваш унікальний тест з маркером -k
#  додайте скірншоти виконання(не забудьте додавати -v, що б я бачив що ви проганяли) і біля скріншотів пропишіть
#  команди які ви використовували.

import time


def test_sleep_1():
    print("я йду спати на 2 секунди")
    time.sleep(2)


def test_sleep_2():
    print("я йду спати на 2 секунди")
    time.sleep(2)


def test_sleep_3():
    print("я йду спати на 2 секунди")
    time.sleep(2)


def test_sleep_4():
    print("я йду спати на 2 секунди")
    time.sleep(2)


def test_unique_name_5():
    print("я йду спати на 2 секунди")
    time.sleep(2)

# pytest test_lesson_11.py -v -n=5
# pytest -k "unique" test_lesson_11.py -v
