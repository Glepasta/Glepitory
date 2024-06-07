import os
import morse_code as morse1

print("Текущая рабочая директория:", os.getcwd())
print("Содержимое директории:", os.listdir())
print("Импортирован модуль morse:", morse1)
print("Атрибуты модуля morse:", dir(morse1))

def main():
    while True:
        print("Выберите действие:")
        print("1. Кодировать текст в азбуку Морзе")
        print("2. Декодировать текст из азбуки Морзе")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == '1':
            text = input("Введите текст для кодирования: ")
            encoded_text = morse1.encode(text)
            print("Закодированный текст: ", encoded_text)
        elif choice == '2':
            encoded_text = input("Введите закодированный текст: ")
            decoded_text = morse1.decode(encoded_text)
            print("Декодированный текст: ", decoded_text)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
