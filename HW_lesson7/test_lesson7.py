from HW_lesson7 import sort_asc
from HW_lesson7 import sort_desc
from HW_lesson7 import sort_words

random_numbers = (3, 764, 8, 12, 45, 111, 678, 267, 33)
random_words = ('sabina', 'toy', 'children', 'understand', 'python')


def test_sort_ask():
    assert sort_asc(random_numbers) == [3, 8, 12, 33, 45, 111, 267, 678, 764]


def test_sort_desc():
    assert sort_desc(random_numbers) == [764, 678, 267, 111, 45, 33, 12, 8, 3]


def test_sort_words():
    assert sort_words(random_words) == ['toy', 'sabina', 'python', 'children', 'understand']
