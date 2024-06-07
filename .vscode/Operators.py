def main():
    # Создание переменных типа bool
    bool_var1 = True
    bool_var2 = False
    
    # Печать типов переменных
    print(f"Тип bool_var1: {type(bool_var1)}")
    print(f"Тип bool_var2: {type(bool_var2)}")
    
    # Логические операции
    print(f"Конъюнкция (True и False): {bool_var1 and bool_var2}")
    print(f"Дизъюнкция (True или False): {bool_var1 or bool_var2}")
    print(f"Инверсия (не True): {not bool_var1}")
    print(f"Инверсия (не False): {not bool_var2}")
    
    # Создание переменных типа int
    int_var1 = 7
    int_var2 = 3
    
    # Операции сравнения
    print(f"int_var1 == int_var2: {int_var1 == int_var2}")
    print(f"int_var1 != int_var2: {int_var1 != int_var2}")
    print(f"int_var1 > int_var2: {int_var1 > int_var2}")
    print(f"int_var1 < int_var2: {int_var1 < int_var2}")
    print(f"int_var1 >= int_var2: {int_var1 >= int_var2}")
    print(f"int_var1 <= int_var2: {int_var1 <= int_var2}")
    
    # Арифметические операции
    print(f"Сложение: {int_var1} + {int_var2} = {int_var1 + int_var2}")
    print(f"Вычитание: {int_var1} - {int_var2} = {int_var1 - int_var2}")
    print(f"Умножение: {int_var1} * {int_var2} = {int_var1 * int_var2}")
    print(f"Деление: {int_var1} / {int_var2} = {int_var1 / int_var2}")
    print(f"Возведение в степень: {int_var1} ** {int_var2} = {int_var1 ** int_var2}")
    print(f"Деление по модулю: {int_var1} % {int_var2} = {int_var1 % int_var2}")
    print(f"Целочисленное деление: {int_var1} // {int_var2} = {int_var1 // int_var2}")

# Запуск функции main() при непосредственном запуске скрипта
if __name__ == "__main__":
    main()