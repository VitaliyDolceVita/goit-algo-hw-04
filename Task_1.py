def total_salary(path):
    total_salary = 0
    num_developers = 0
    #path = path.replace("\\", "\\\\")
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на прізвище розробника та його заробітну плату
                name, salary = line.strip().split(',')
                # Додаємо заробітну плату до загальної суми
                total_salary += int(salary)
                # Збільшуємо лічильник розробників
                num_developers += 1
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

    # Обчислюємо середню зарплату
    if num_developers > 0:
        average_salary = total_salary / num_developers
    else:
        average_salary = 0

    return total_salary, average_salary

# Приклад використання
total, average = total_salary(r"C:\Users\Usuario\Desktop\Bib\salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
