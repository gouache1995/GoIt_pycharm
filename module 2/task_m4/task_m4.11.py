def is_valid_password(password):
    if len(password) < 8:
        return False

    # Ініціалізація змінних для перевірки вимог
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Перевірка наявності літер у верхньому та нижньому регістрах та цифр
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    # Перевірка виконання всіх трьох вимог
    if has_uppercase and has_lowercase and has_digit:
        return True
    else:
        return False

# Приклад використання
input_password = "SecurePass123"
result = is_valid_password(input_password)
if result:
    print("Пароль відповідає вимогам на надійність.")
else:
    print("Пароль не відповідає вимогам на надійність.")