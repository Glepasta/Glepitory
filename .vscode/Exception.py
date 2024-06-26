def safe_divide_input():
    """
    Функция запрашивает два числа у пользователя и выполняет деление,
    исключая деление на ноль.
    """
    try:
        # Запрашиваем ввод делимого и делителя
        a = float(input("Введите делимое (число, которое делится): "))
        b = float(input("Введите делитель (число, на которое делят): "))
        
        # Выполняем деление с проверкой на деление на ноль
        if b == 0:
            return "Ошибка: Деление на ноль невозможно."
        else:
            return f"Результат деления {a} на {b} равен: {a / b}"
    
    except ValueError:
        return "Ошибка: Пожалуйста, введите числовое значение."

# Пример использования функции
if __name__ == "__main__":
    print(safe_divide_input())