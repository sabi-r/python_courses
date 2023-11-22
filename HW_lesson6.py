# Візьміть дві задачі з попередніх уроків, перша легка по вирішенню(декілька стрічок),
# друга більш складна і перепишіть їх на функції. Памятайте про Атамарність та god object.
# Там де написано що користувач має щось ввести то перероблюємо на функція приймає.
# Подивіться може можна за допомогою функції спростити код. В домашку вставте будь ласка опис задачі
# (далі(один з наступних уроків) буде домашка вашу домашку покрити тестами, але ми трохи поміняємо варіанти).

# 14 Податки
# Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
#  програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# Виведіть на екран скільки треба податків сплатити. Не забудьте ЄСВ(4422)

# def calculate_tax(salary: int | float, single_tax: int | float):
#     tax_to_pay = (salary * (single_tax / 100)) + 4422
#     return tax_to_pay
#
# user_salary = float(input("Введіть зарплату:"))
# user_single_tax = float(input("Введіть процент податку:"))
#
# result = calculate_tax(salary=user_salary, single_tax=user_single_tax)
# print(result)
#
# _______________________________________________________________________________________________________________
#
# Задача 2
#
# Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині
#
# що б можна було скласти список продуктів та коли купуєш викреслювати(для викреслення питайте номер елемента,
# що б видалити по індексу треба його передати в pop list_a.pop(0) -
# видалить нульовий індекс, памятайте що користувач не знає що в нас індекси починаються з нуля)
#
# Також нам відомо що цей список має пять або більше елементів.
#
# Після кожного видалення елементу виводьте наш оновлений список.
#
# Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти,
# якщо пусти то напишіть про це.
#
# Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик.
# і виведіть їх на екран.
# Але цього разу вже без видалень.
#
# def add_product(internal_input: str):
#     internal_list = internal_input.split()
#     print(f"Ось ваш список продуктів: {internal_list}")
#     return internal_list
#
#
# def delete_product(internal_index: int, internal_list: list):
#     if 0 < internal_index <= len(internal_list):
#         internal_list.pop(internal_index - 1)
#         print(f"Ось ваш оновлений список продуктів: {internal_list}")
#         return internal_list
#
#
# def manage_products(user_list: str):
#     user_list = add_product(internal_input=user_list)
#
#     while len(user_list) > 0:
#         user_index = int(input("Який продукт ви вже купили?"))
#         delete_product(internal_index=user_index, internal_list=user_list)
#
#     if len(user_list) == 0:
#         user_input = input("Введіть список продуктів через пробіл")
#         user_list = add_product(internal_input=user_input)
#     else:
#         if len(user_list) > 0:
#             user_index = int(input("Який продукт ви вже купили?"))
#             delete_product(internal_index=user_index, internal_list=user_list)
#
#
# user_input = input("Введіть список продуктів через пробіл")
# manage_products(user_list=user_input)


