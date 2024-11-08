import string
import secrets


def generate_password(length=12, include_letters=True, include_digits=True, include_symbols=True):
    characters = string.ascii_letters + string.digits + string.punctuation # Инициализация строки для хранения символов, из которых будет сгенерирован пароль
    if include_letters:
        characters += string.ascii_letters + string.digits + string.punctuation
        if include_digits:
            characters += string.ascii_letters + string.digits + string.punctuation
            if include_symbols:
                characters += string.ascii_letters + string.digits + string.punctuation
    characters += string.punctuation
    if not characters:
        raise ValueError("Не выбраны символы для генерации пароля.")
    # Генерация пароля путем случайного выбора символов из списка characters длиной length
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password


def get_user_preferences():
    print("Давайте настроим генератор паролей!")
    length = int(input("Введите длину пароля: "))
    # Получение от пользователя настроек включения букв, цифр и спецсимволов, приведение к нижнему регистру и сравнение с 'да'
    include_letters = input("Включать ли буквы (да/нет): ").lower() == 'да'
    include_digits = input("Включать ли цифры (да/нет): ").lower() == 'да'
    include_symbols = input("Включать ли спецсимволы (да/нет): ").lower() == 'да'
    mask_password = input("Замаскировать пароль при его выводе на экран? (да/нет): ").lower() == 'да'
    return length, include_letters, include_digits, include_symbols, mask_password


def save_passwords(passwords, filename="passwords.txt"):
    with open(filename, 'a') as file: # Открытие файла для добавления
        file.write(passwords + '\n')
        for password in passwords:  # Перебор всех паролей в списке
            file.write(password + '\n')  # Запись пароля в файл с добавлением новой строки
    print(f"Пароль успешно сохранен в файл {filename}.")


def assess_password_strength(password):
    length = len(password)
    has_letters = any(char.isalpha() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_symbols = any(char in string.punctuation for char in password)
    strength = sum([length >= 8, has_letters, has_digits, has_symbols])
    print("Оценка сложности пароля:", strength, "из 4")
    return strength


def main():
    # Получение пользовательских настроек для генерации пароля
    length, include_letters, include_digits, include_symbols, mask_password = get_user_preferences()
    # Генерация пароля на основе пользовательских настроек
    password = generate_password(length, include_letters, include_digits, include_symbols)
    if mask_password:
        print("Ваш новый пароль:", password[0] + "*" * (len(password) - 1))
    else:
        print("Ваш новый пароль:", password)
    save_to_file = input("Хотите сохранить пароль в файл? (да/нет): ").lower()
    if save_to_file == "да":
        save_passwords([password])
        print("Пароль успешно сохранен в файл 'passwords.txt'")
    assess_password_strength(password)


if __name__ == "__main__":
    main()
