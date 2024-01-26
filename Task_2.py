def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на ідентифікатор, ім'я та вік кота
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return cats_info

# Приклад використання
cats_info = get_cats_info(r"C:\Users\Usuario\Desktop\Bib\cats_file.txt")
print(cats_info)
