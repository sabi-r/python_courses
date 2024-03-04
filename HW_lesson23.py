import random
import string


def generate_password(length, use_cyrillic=False, use_latin=True, use_digits=True, use_symbols=False):
    characters = ''
    if use_cyrillic:
        characters += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if use_latin:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one type of characters should be selected")

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    length = int(input("Enter the length of the password: "))
    use_cyrillic = input("Use Cyrillic characters? (y/n): ").lower() == 'y'
    use_latin = input("Use Latin characters? (y/n): ").lower() == 'y'
    use_digits = input("Use digits? (y/n): ").lower() == 'y'
    use_symbols = input("Use symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_cyrillic, use_latin, use_digits, use_symbols)
    print("Generated password:", password)


if __name__ == "__main__":
    main()
