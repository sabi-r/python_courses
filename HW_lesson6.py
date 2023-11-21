# Візьміть дві задачі з попередніх уроків, перша легка по вирішенню(декілька стрічок),
# друга більш складна і перепишіть їх на функції. Памятайте про Атамарність та god object.
# Там де написано що користувач має щось ввести то перероблюємо на функція приймає.
# Подивіться може можна за допомогою функції спростити код. В домашку вставте будь ласка опис задачі
# (далі(один з наступних уроків) буде домашка вашу домашку покрити тестами, але ми трохи поміняємо варіанти).

# 14 Податки
# Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
# програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# Виведіть на екран скільки треба податків сплатити. Не забудьте ЄСВ(4422)

# salary = float(input("Введіть зарплату:"))
# single_tax = float(input("Введіть процент податку:"))
# euv = 4422
#
# tax_to_pay = (salary * (single_tax / 100)) + euv
# print(tax_to_pay)


def calculate_tax(salary, single_tax):
    tax_to_pay = (salary * (single_tax / 100)) + 4422
    return tax_to_pay

user_salary = float(input("Введіть зарплату:"))
user_single_tax = float(input("Введіть процент податку:"))

result = calculate_tax(salary=user_salary, single_tax=user_single_tax)
print(result)










# function Атомарність одна функція одна дія VS god object
def foo(number_1, number_2):
    result = number_1 * number_2
    return result



# def my_print():
#     print("старт роботи")
# my_print()


# def foo(name, age):
#     print(f"my name {name}, I  {age} y.o.")
#
# foo("Pavlo", 67)
# foo(67, "Pavlo")  # порядок важливий
# foo(name="Ярослав", age=16)  # Найбільш коректний
# foo(age=16, name="Ярослав")
#
#
# my name Pavlo, I  67 y.o.
# my name 67, I  Pavlo y.o.
# my name Ярослав, I  16 y.o.
# my name Ярослав, I  16 y.o.

#
# def my_print(string):
#     new_string = f"{'#' * 30}\n{string}\n{'#' * 30}"
#     return new_string
#
#
# my_string = "next level"
# # new_result = my_print(string=my_string)
#
# print(new_result)