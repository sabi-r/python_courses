# Виберіть який з наступних магічних методів і реалізуйте його в простому класі:
# lt: To check if one object is less than another.
# Жодного з цих методів ми не розглядали на уроці, але вони працюють ідентично до метода ___eq__ який ми розглянули на уроці.
# Тобто вам треба буде змінити всього дві букви.
# І написати свою логіку яку ви хочте.
#
# Створіть два обьєта класа в якому ви це реалізували і зробіть перевірку що все працює


class A:
    def __init__(self, text):
        self.text = text

    def __lt__(self, other):  # <
        if not isinstance(other, type(self)):
            raise TypeError
        return len(self.text) < len(other.text)


obj_1 = A("Hello")
obj_2 = A("Hello hello")
print(obj_1 < obj_2)  # порівнюємо об'єкти