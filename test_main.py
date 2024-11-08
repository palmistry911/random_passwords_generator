import unittest
from unittest.mock import patch
import os
from main import (
    generate_password,
    get_user_preferences,
    save_passwords,
    assess_password_strength,
)


class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password(self):
        # Тестирование функции generate_password()

        # Case 1: Тестирование с параметрами по умолчанию
        password = generate_password()
        self.assertEqual(len(password), 12)  # Проверка длины пароля (должна быть 12 символов)

        # Case 2: Тестирование с определенными параметрами
        password = generate_password(length=8, include_letters=False, include_digits=True, include_symbols=True)
        self.assertEqual(len(password), 8)  # Проверка длины пароля (должна быть 8 символов)
        self.assertTrue(any(char.isdigit() for char in password))  # Проверка, содержит ли пароль хотя бы одну цифру

        # Case 3: Максимальная длина пароля (например, 100 символов)
        password = generate_password(length=100, include_letters=True, include_digits=True, include_symbols=True)
        self.assertEqual(len(password), 100)
        # Case 4: Без букв, только цифры и спецсимволы
        password = generate_password(length=10, include_letters=False, include_digits=True, include_symbols=True)
        self.assertTrue(all(char.isdigit() or char in string.punctuation for char in password))
        # Case 5: Без букв и спецсимволов, только цифры
        password = generate_password(length=8, include_letters=False, include_digits=True, include_symbols=False)
        self.assertTrue(password.isdigit())

    @patch('main.input', side_effect=['12', 'нет', 'да', 'нет', 'да'])
    def test_get_user_preferences(self):
        # Тестирование функции get_user_preferences()

        # Тестирование пользовательского ввода
        # Предполагаем, что эта функция возвращает значения без ошибок
        length, include_letters, include_digits, include_symbols, mask_password = get_user_preferences()
        self.assertIsInstance(length, int)  # Проверка, является ли длина целым числом
        self.assertIsInstance(include_letters, bool)  # Проверка, является ли включение букв логическим значением
        self.assertIsInstance(include_digits, bool)  # Проверка, является ли включение цифр логическим значением
        self.assertIsInstance(include_symbols, bool)  # Проверка, является ли включение символов логическим значением
        self.assertIsInstance(mask_password, bool)  # Проверка, является ли замаскирование пароля логическим значением

    def test_save_passwords(self):
        # Тестирование функции save_passwords()

        # Создание временного файла для тестирования
        filename = "test_passwords.txt"
        passwords = ["test_password_1", "test_password_2", "test_password_3"]
        save_passwords(passwords, filename)

        # Проверка сохраненных паролей
        with open(filename, "r") as file:
            saved_passwords = file.readlines()
        saved_passwords = [password.strip() for password in saved_passwords]
        self.assertEqual(saved_passwords, passwords)  # Проверка, соответствуют ли сохраненные пароли ожидаемым

    def test_assess_password_strength(self):
        # Тестирование функции assess_password_strength()

        # Тестирование на паролях разной сложности
        password_weak = "1234"
        password_strong = "Str0ngP@ssw0rd!"
        self.assertEqual(assess_password_strength(password_weak), 1)  # Проверка слабого пароля
        self.assertEqual(assess_password_strength(password_strong), 4)  # Проверка сильного пароля
        # Слабый пароль только из одной буквы
        password_very_weak = "a"
        self.assertEqual(assess_password_strength(password_very_weak), 1)
        # Средний пароль (буквы и цифры, но короткий)
        password_medium = "abc123"
        self.assertEqual(assess_password_strength(password_medium), 2)
        # Длинный и сложный пароль
        password_very_strong = "A1b2C3!d4E5f6*G7h8"
        self.assertEqual(assess_password_strength(password_very_strong), 4)


if __name__ == '__main__':
    unittest.main()
