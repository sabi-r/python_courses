# # Задача 1
# #
# # Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл, точна кількість не вказана.
# # Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# #
# # Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і потім віднімаєте суму
# # або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
# #
# # * завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня, якщо менше.
# # то тоді просто відкидаємо копійки від ціни.
#
# amounts_products = input("Яка вартість покупок?: ").split()
# total_cost = 0
# tax_rate = 6.5
# for element in amounts_products:
#     total_cost += float(element)
# tax_amount = (tax_rate / 100) * total_cost
# total_cost_with_tax = total_cost + tax_amount
# coupon = input("Чи є у вас купон на знижку? (Так/Ні): ")
# if coupon == 'так':
#     coupon_type = input("Купон на суму чи на відсоток? (сума/відсоток): ")
#     if coupon_type == 'сума':
#         coupon_value = float(input("Введіть значення знижки: "))
#         final_cost = total_cost_with_tax - coupon_value
#         print(f"Кінцева сума з урахуванням знижки: {final_cost} грн")
#     elif coupon_type == 'відсоток':
#         coupon_value = float(input("Введіть значення знижки: "))
#         coupon_amount = (coupon_value / 100) * total_cost_with_tax
#         final_cost = total_cost_with_tax - coupon_amount
#         print(f"Кінцева сума з урахуванням знижки: {final_cost} грн")
# elif coupon == 'ні':
#     print(f"Кінцева сума без урахуванням знижки: {total_cost_with_tax} грн")
# else:
#     print("Неправильний тип знижки. Введіть 'сума' або 'відсоток'.")

# ___________________________________________________________________________________________________________________________
#
# #  Задача 2 ( переробила з HW_lesson3.py
#
# list_products = input("Введіть ваші продукти через пробіл").split()
# print(f"Ось ваш список продуктів: {list_products}")
# while len(list_products) > 0:
#     del_product = int(input("Який продукт ви вже купили?"))
#     if del_product > 0 and del_product <= len(list_products):
#         list_products.pop(del_product - 1)
#         print(f"Ось ваш оновлений список продуктів: {list_products}")
# if len(list_products) == 0:
#     list_products = input("Давайте додамо ще продуктів. Додайте продукти").split()
#     print(f"Ось ваш фінальний список продуктів {list_products}")
# elif len(list_products) > 0:
#     print(f"Ви ще не все купили, ось список продуктів : {list_products}")
# else:
#     print("Такого бути не може")
#

# Задача  3
#
# Напишіть програму Банкомат.
# Втсановіть пін код для користувача(зробимо це константою).

# Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована.
# Використовуйте цикл while.

PIN_CODE = 1122
input_pin = int(input("Введіть PIN, у вас 3 спроби: "))
while input_pin == PIN_CODE:
    input_pin(PIN_CODE - 1)
    print("Ви увійшли у систему")
if input_pin > 3:
    input_pin.pop(PIN_CODE - 1)
    print("Карта заблокована")
if input_pin == 0:
    input_pin = input("Ви не ввели PIN, спробуйте ще раз: ")
    print(f"Ось ваш фінальний список продуктів ")



# Задача 4
#
# Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
#
# name = "оЛенА"
#
# age = 21
#
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
#
# format_string = тут ваш код формата формат стрінг  | повино вийти -> Я Олена, мені 21 рік
#
# print(f_string)
#
# print(format_string)