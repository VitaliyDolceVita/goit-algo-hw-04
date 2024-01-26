# Створюємо словник для зберігання контактів. Ключі - імена, значення - номери телефонів.
contacts = {}

# Функція для розбору введених команд користувача.
def parse_input(command):
    # Перетворюємо введену команду у нижній регістр для зручності порівняння.
    parts = command.lower().split()
    # Перевіряємо, яка команда була введена та викликаємо відповідну функцію.
    if parts[0] == "hello":
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

# Функція для додавання нового контакту до словника.
def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added."

# Функція для зміни номера телефону існуючого контакту.
def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

# Функція для відображення номера телефону за ім'ям контакту.
def show_phone(name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

# Функція для відображення всіх контактів.
def show_all():
    if contacts:
        # Формуємо рядок з усіма контактами для виводу.
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

# Основна функція для управління основним циклом обробки команд.
def main():
    while True:
        # Зчитуємо введену користувачем команду.
        command = input("Enter command: ")
        # Розбираємо введену команду та отримуємо відповідь.
        response = parse_input(command)
        # Виводимо відповідь користувачеві.
        print(response)
        # Якщо користувач ввів "exit" або "close", завершуємо виконання програми.
        if response == "Good bye!":
            break

# Перевіряємо, чи цей скрипт є основним і викликаємо функцію main.
if __name__ == "__main__":
    main()

