def get_cats_info(path):  # Визначаємо функцію
    cats_info = []  # Створюємо пустий список для збереження словників з данними
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')  # Розділяємо рядок на ідентифікатор, ім'я та вік кота
                cat_info = {  #  Створюємо словник для зберігання данних з відповідними ключами
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)  # Додаємо словник до списку
    except FileNotFoundError:  # Обробляємо винятки, помилки
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return cats_info

# Приклад використання
cats_info = get_cats_info(r"C:\Users\Usuario\Desktop\Bib\cats_file.txt")
print(cats_info)
