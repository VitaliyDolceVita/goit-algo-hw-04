contacts = {}  # Створюємо словник для зберігання контактів. Ключі - імена, значення - номери телефонів.

def parse_input(command):  # Функція для розбору введених команд користувача.
    parts = command.lower().split()   # Перетворюємо введену команду у нижній регістр для зручності порівняння.
    if parts[0] == "hello":  # Перевіряємо, яка команда була введена та викликаємо відповідну функцію.
        return "How can I help you?"
    elif parts[0] == "add" and len(parts) == 3:
        return add_contact(parts[1], parts[2])
    elif parts[0] == "change" and len(parts) == 3:
        return change_contact(parts[1], parts[2])
    elif parts[0] == "phone" and len(parts) == 2:
        return show_phone(parts[1])
    elif parts[0] == "all":
        return show_all()
    elif parts[0] == "exit" or parts[0] == "close":
        return "Good bye!"
    else:
        return "Invalid command."

def add_contact(name, phone):  # Функція для додавання нового контакту до словника.
    contacts[name] = phone
    return "Contact added."

def change_contact(name, new_phone):  # Функція для зміни номера телефону існуючого контакту.
    if name in contacts:  # Якщо
        contacts[name] = new_phone  # Записуєм значення нового телефону по ключу "name".
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(name):  # Функція для відображення номера телефону за ім'ям контакту.
    if name in contacts:  # Якщо введене ім'я є в контактах
        return contacts[name]  # Повертаємо значення контакту
    else:  # Якщо імені немає в списку 
        return "Contact not found."

def show_all():  # Функція для відображення всіх контактів.
    if contacts:  # Якщо контакти є
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])   # Формуємо рядок з усіма контактами для виводу.
    else:  # Якщо контактів нема 
        return "No contacts found."  


def main():  # Основна функція для управління основним циклом обробки команд.
    while True:  # Запускаємо безкінечний цикл.
        command = input("Enter command: ")  # Зчитуємо введену користувачем команду. 
        response = parse_input(command)  # Розбираємо введену команду та отримуємо відповідь.
        print(response)    # Виводимо відповідь користувачеві.
        if response == "Good bye!":    # Якщо користувач ввів "exit" або "close", завершуємо виконання програми.
            break


if __name__ == "__main__":  # Перевіряємо, чи цей скрипт є основним і викликаємо функцію main.
    main()

