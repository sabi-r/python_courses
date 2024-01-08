# 1) Напишіть ліст компрехеншин який формує список всіх чисел від 34 до 121 які діляться націло на 3 та на 2

divisible_numbers = [x for x in range(34, 122) if x % 3 == 0 and x % 2 == 0]
print(divisible_numbers)

# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення - звичайні методи.
# і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.

class Calculator:
    @staticmethod
    def greeting_message():
        print("Привіт, я калькулятор!")

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Ділення на нуль неможливе.")
        return a / b
    