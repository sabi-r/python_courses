import random
import string


def generate_password(alphabet, length):
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password


def main():
    print("Привіт! Ця програма генерує паролі.")
    print("Виберіть тип алфавіту для паролю:")
    print("1. Кирилиця")
    print("2. Латиниця")
    print("3. Цифри")
    choice = input("Ваш вибір: ")

    if choice == '1':
        alphabet_case = input(
            "Оберіть регістр для кирилиці: (Великі - 'В', Малі - 'М', Великі і Малі - 'ВМ'): ").upper()
        if alphabet_case == 'В':
            alphabet = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
        elif alphabet_case == 'М':
            alphabet = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
        elif alphabet_case == 'ВМ':
            alphabet = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя' + 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
        else:
            print("Невірний вибір.")
            return
    elif choice == '2':
        alphabet_case = input(
            "Оберіть регістр для латиниці: (Великі - 'В', Малі - 'М', Великі і Малі - 'ВМ'): ").upper()
        if alphabet_case == 'В':
            alphabet = string.ascii_uppercase
        elif alphabet_case == 'М':
            alphabet = string.ascii_lowercase
        elif alphabet_case == 'ВМ':
            alphabet = string.ascii_lowercase + string.ascii_uppercase
        else:
            print("Невірний вибір.")
            return
    elif choice == '3':
        alphabet = string.digits
    else:
        print("Невірний вибір.")
        return

    length = int(input("Введіть довжину паролю: "))
    password = generate_password(alphabet, length)
    print("Ваш пароль:", password)


if __name__ == "__main__":
    main()
