# Задача 1
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
# Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти, якщо пусти то напишіть про це.
#
# Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик. і виведіть їх на екран.
# Але цього разу вже без видалень.
#
# кроки:
#
# Спочатку пропонуємо користувачу ввести продукти.
# Робимо 5 запитів на видалення
# Перевіряємо корзину
# Пропонуємо додати продукти
# Виводмо список і прощаємось


list_products = []

product = input("Введіть продукт №1:")
list_products.append(product)

product = input("Введіть продукт №2:")
list_products.append(product)

product = input("Введіть продукт №3:")
list_products.append(product)

product = input("Введіть продукт №4:")
list_products.append(product)

product = input("Введіть продукт №5:")
list_products.append(product)

print(f"Ось ваш список продуктів: {list_products}")

del_product = int(input("Який продукт ви вже купили?"))
if del_product > 0 and del_product <= len(list_products):
    list_products.pop(del_product - 1)
    print(f"Ось ваш оновлений список продуктів: {list_products}")

del_product = int(input("Який продукт ви вже купили?"))
if del_product > 0 and del_product <= len(list_products):
    list_products.pop(del_product - 1)
    print(f"Ось ваш оновлений список продуктів: {list_products}")

del_product = int(input("Який продукт ви вже купили?"))
if del_product > 0 and del_product <= len(list_products):
    list_products.pop(del_product - 1)
    print(f"Ось ваш оновлений список продуктів: {list_products}")

del_product = int(input("Який продукт ви вже купили?"))
if del_product > 0 and del_product <= len(list_products):
    list_products.pop(del_product - 1)
    print(f"Ось ваш оновлений список продуктів: {list_products}")

del_product = int(input("Який продукт ви вже купили?"))
if del_product > 0 and del_product <= len(list_products):
    list_products.pop(del_product - 1)
    print(f"Ось ваш оновлений список продуктів: {list_products}")

if len(list_products) == 0:
    product = input("Давайте додамо ще продуктів. Додайте продукти")
    list_products.append(product)

if len(list_products) < 5:
    product = input("Давайте додамо ще продуктів. Додайте продукт")
    list_products.append(product)

if len(list_products) < 5:
    product = input("Давайте додамо ще продуктів. Додайте продукт")
    list_products.append(product)

if len(list_products) < 5:
    product = input("Давайте додамо ще продуктів. Додайте продукт")
    list_products.append(product)

if len(list_products) < 5:
    product = input("Давайте додамо ще продуктів. Додайте продукт")
    list_products.append(product)

print(f"Ось ваш фінальний список продуктів {list_products}")
