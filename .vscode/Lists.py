# Создание списка
my_list = [None, 42, 3.14, "Hello", [1, 2, 3], (4, 5, 6), {"key": "value"}]

# Вывод типа каждого элемента
for item in my_list:
    print(f"Тип элемента: {type(item)}")

# Удаление последнего элемента
last_element = my_list.pop()
print("Удаленный элемент:", last_element)

# Строковая переменная с ФИО
fio = "Паутов Глеб Алексеевич"

# Создание списка из букв ФИО
letters = list(fio)
print("Список букв ФИО:", letters)

# Создание строки из списка букв ФИО
fio_from_list = ''.join(letters)
print("ФИО из списка:", fio_from_list)

# Печать порядкового номера и символа в ФИО
for index, char in enumerate(fio, start=1):
    print(f"Порядковый номер: {index}, Символ: {char}")

# Печать количества символов 'а' в списке букв ФИО
count_a = letters.count('а')
print("Количество символов 'а':", count_a)