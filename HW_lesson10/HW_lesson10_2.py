# Задача 2
# Візьміть задачу з минулого уроку(
# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома методами
# ) модернізуйте її так що кожний раз коли ми її запускаємо те що ми туди передаєм та результат повинно записуватись в файл log.txt
# Зверніть увагу на те що в файл повинно дозаписуватись, а не затератись.
# Уявіть що ця функція являється легасі кодом і ви її не можете змінювати,
# тому потрібно використовувати декоратор. Я хотів би бачити таку реалізацію в домашці три функції:
# функція з минулого уроку
# функція що записую текст
# і декоратор

def result_logs(func):
    def wrapper(*args):
        result = func(*args)
        with open('log.txt', 'a') as file:
            file.write(f"Arguments:{args},result:{result}")
        return result

    return wrapper


@result_logs
def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result


result = add_three_numbers(3, 4, 5)
print(result)
