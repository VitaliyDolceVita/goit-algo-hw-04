import os  # Імпортуємо необхідні модулі
import sys
from colorama import Fore


def list_files_and_directories(directory, indent=""):
    try:
        with os.scandir(directory) as entries:
            for entry in entries: # Проходимось по елементах 
                if entry.is_dir():  # Якщо обь'єкт є папкою 
                    print(indent + Fore.MAGENTA + entry.name )  # Виводимо відступ, назву папки кольору магента
                    list_files_and_directories(entry.path, indent + "  ")  # збільшуємо відступ при кожному рекурсивному виклику функції
                else:
                    print(indent + Fore.GREEN + entry.name)  # Виводи відступ, назву файла зелеого кольору
    except FileNotFoundError:  # Обробляємо помилки і красим їх вивід в червоний колір
        print(Fore.RED + f"Директорія {directory} не знайдена.")
    except PermissionError:
        print(Fore.RED + f"Немає доступу до директорії {directory}.")
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")


def main():
    if len(sys.argv) != 2:  # яккщо кількість аргументів командного рядка не дорівнює двом
        print("Використання: python Task_3.py /шлях/до/директорії")   # Виводим приклад вводу користувачем
        sys.exit(1)  #  Виходимо з програми з кодом помилки 1

    directory = sys.argv[1]  #  шлях до директорії з першого аргументу командного рядка зберігаєм в змінній
    if not os.path.isdir(directory):  #  Провіряємо чи об'єкт папка
        print(f"{directory} не є директорією.")   #  Повідомляємо користувача 
        sys.exit(1)  # Вихід з програми з кодом помилки 1

    print(f"Структура директорії {directory}:")  #  Друкуєм структуру папак і файлів
    list_files_and_directories(directory)   # Викликаэмо  функцію


if __name__ == "__main__":  # Перевіряємо чи файл не викликається як модуль
    main()
    
