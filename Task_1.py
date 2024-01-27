def total_salary(path):
    total_salary = 0
    num_developers = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:  # Відкриваєм файл через контекстний менеджер, вказуєм кодування utf-8
            for line in file:  # Проходимся по рідках файла
                name, salary = line.strip().split(',')  # Розділяємо рядок на прізвище розробника та його заробітну плату
                total_salary += int(salary)  # Додаємо заробітну плату до загальної суми
                num_developers += 1  # Збільшуємо лічильник розробників
    except FileNotFoundError:  # Обробляємо помилки
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
