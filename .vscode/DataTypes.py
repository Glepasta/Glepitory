def main():
    # Создание переменных различных типов
    none_var = None
    int_var = 42
    float_var = 3.14
    str_var = "Hello, World!"
    list_var = [1, 2, 3, 4, 5]
    tuple_var = (10, 20, 30, 40, 50)
    dict_var = {"key1": "value1", "key2": "value2", "key3": "value3"}
    set_var = {100, 200, 300, 400}

    # Печать типов переменных
    print(f"Тип none_var: {type(none_var)}")
    print(f"Тип int_var: {type(int_var)}")
    print(f"Тип float_var: {type(float_var)}")
    print(f"Тип str_var: {type(str_var)}")
    print(f"Тип list_var: {type(list_var)}")
    print(f"Тип tuple_var: {type(tuple_var)}")
    print(f"Тип dict_var: {type(dict_var)}")
    print(f"Тип set_var: {type(set_var)}")

    # Изменение типов для int и float
    int_as_float = float(int_var)
    print(f"int_var как float: {int_as_float} (тип: {type(int_as_float)})")

    float_as_int = int(float_var)
    print(f"float_var как int: {float_as_int} (тип: {type(float_as_int)})")

    # Изменение типов для float и str
    float_as_str = str(float_var)
    print(f"float_var как str: '{float_as_str}' (тип: {type(float_as_str)})")

    str_as_float = float(float_as_str)  # Обратное преобразование (если строка представляет число)
    print(f"str (из float_var) как float: {str_as_float} (тип: {type(str_as_float)})")

    # Печать размера для str, list, tuple, dict, set
    print(f"Размер str_var: {len(str_var)}")
    print(f"Размер list_var: {len(list_var)}")
    print(f"Размер tuple_var: {len(tuple_var)}")
    print(f"Размер dict_var: {len(dict_var)}")
    print(f"Размер set_var: {len(set_var)}")

    # Печать первого и последнего элементов для str, list, tuple
    print(f"Первый элемент str_var: {str_var[0]}, последний элемент: {str_var[-1]}")
    print(f"Первый элемент list_var: {list_var[0]}, последний элемент: {list_var[-1]}")
    print(f"Первый элемент tuple_var: {tuple_var[0]}, последний элемент: {tuple_var[-1]}")

    # Печать элементов кроме первого и последнего для str, list, tuple
    print(f"Элементы str_var кроме первого и последнего: {str_var[1:-1]}")
    print(f"Элементы list_var кроме первого и последнего: {list_var[1:-1]}")
    print(f"Элементы tuple_var кроме первого и последнего: {tuple_var[1:-1]}")

    # Печать значения одного из ключей для dict
    print(f"Значение для 'key1' в dict_var: {dict_var['key1']}")

# Запуск функции main() при непосредственном запуске скрипта
if __name__ == "__main__":
    main()