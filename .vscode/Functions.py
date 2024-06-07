def print_hello():
    print("Привет, мир!")

# Вызов функции
print_hello()

def print_name(name):
    print(name)

# Вызов функции с аргументом "Вася"
print_name("Глебстер")

def calculate_discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D

# Вызов функции с аргументами a=3, b=4, c=5
discriminant = calculate_discriminant(3, 4, 5)
print("Дискриминант:", discriminant)

def ask_user_info():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    return name, age

# Вызов функции
user_name, user_age = ask_user_info()
print("Имя:", user_name)
print("Возраст:", user_age)

def get_letter_by_number(number):
    if number <= 33:
        return chr(ord('а') + number - 1)
    else:
        print("Указано неправильное число!")

# Вызов функции с аргументом 5
letter = get_letter_by_number(5)
print("Буква по номеру:", letter)