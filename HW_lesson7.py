# # ДЗ 7 Уроку
# #
# # Створіть два файли
# # в 1-му напишіть такі функції:
# # 1) сортування списка по зростанню числа, від меншого до більшого. Функція приймає список з чисел і повертає відсортований список.
# # 2) сортування списка на спад, від  більшого до меншого. Функція приймає список з чисел і повертає відсортований список.
# # 3) сортування за кількістю букв у слові. Функція приймає список з слів і повертає відсортований список.
# #
# # 2-ий файл з трьома тестами який буде тестити ці три функції. В кожному тесті 1 тест.
# # В тестових функціях ми ставимо типізацію. В першому файлі в всіх функціях проставляємо що приймає і що повертає.
# # Встановіть собі пайтест і прораньте. До домашки отрім кода додайте скріншот прогона тестів.
#
#
# def sort_asc(tuple_numbers: tuple) -> list:
#     sorted_numbers = sorted(list(tuple_numbers))
#     print(sorted_numbers)
#     return sorted_numbers
#
#
# def sort_desc(tuple_numbers: tuple) -> list:
#     sorted_numbers = sorted(list(tuple_numbers), reverse=True)
#     print(sorted_numbers)
#     return sorted_numbers
#
#
# def sort_words(tuple_words: tuple) -> list:
#     sorted_words = sorted(list(tuple_words), key=len)
#     print(sorted_words)
#     return sorted_words
#
#
# random_numbers = (3, 764, 8, 12, 45, 111, 678, 267, 33)
# random_words = ('sabina', 'toy', 'children', 'understand', 'python')
#
# sort_asc(tuple_numbers=random_numbers)
# sort_desc(tuple_numbers=random_numbers)
# sort_words(tuple_words=random_words)
