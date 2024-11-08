# Генератор случайных паролей
## Описание проекта
Данный проект представляет собой инструмент для генерации паролей с возможностью настройки длины, включения букв, цифр и специальных символов. 
Проект состоит из основного файла , который содержит функции для генерации паролей и взаимодействия с пользователем.
# Структура проекта:
## ` generate_password `
Генерирует случайный пароль заданной длины с возможностью включения букв, цифр и специальных символов.
   - Параметры:
     -  (int) — длина генерируемого пароля (по умолчанию 12).
     -  (bool) — включать ли буквы в пароль (по умолчанию ).
     -  (bool) — включать ли цифры в пароль (по умолчанию ).
     -  (bool) — включать ли специальные символы в пароль (по умолчанию ).
 Исключения:
Вызывает `ValueError`, если не выбраны никакие значения

   - Возвращаемое значение: возвращает строку, представляющую сгенерированный пароль.
     
## `get_user_preferences`
Назначение: Собирает настройки генерации пароля от пользователя через ввод данных.
Входные данные: Функция не принимает параметры.
Выходные данные: возвращает кортеж из пяти элементов: длина пароля, необходимость включения букв, цифр и символов, а также флаг маскирования пароля при выводе.

## `main `
Основная функция, которая вызывает `get_user_preferences`, а затем использует эти предпочтения для генерации пароля с помощью `generate_password`.

## `save_passwords`
Назначение: Сохраняет сгенерированный пароль в файл.
Входные параметры:
`passwords (str)`: Строка с паролем или список паролей для сохранения.
`filename (str, по умолчанию "passwords.txt")`: Имя файла для сохранения


# Использование приложения:
Запустите файл, и функция `get_user_preferences` предложит настроить генерацию пароля, указав его длину, а также необходимость включения символов разных типов.
Вызовите `generate_password` с полученными настройками, чтобы получить сгенерированный пароль.
Если требуется сохранить пароль, передайте его в функцию `save_passwords`.
# Как запустить тесты
Чтобы запустить юнит-тесты для проекта, выполните следующую команду:
`python -m unittest test_main.py`
Это запустит все тесты и проверит их корректность.

Этот генератор позволяет гибко настраивать пароли и сохранять их в отдельном файле для дальнейшего использования
