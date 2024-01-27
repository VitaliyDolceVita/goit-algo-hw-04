import os
import sys
from colorama import Fore


def list_files_and_directories(directory, indent=""):
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_dir():
                    entry.name
                    print(indent + Fore.MAGENTA + entry.name )
                    list_files_and_directories(entry.path, indent + "  ")
                else:
                    print(indent + Fore.GREEN + entry.name)
    except FileNotFoundError:
        print(Fore.RED + f"Директорія {directory} не знайдена.")
    except PermissionError:
        print(Fore.RED + f"Немає доступу до директорії {directory}.")
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python Task_3.py /шлях/до/директорії")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"{directory} не є директорією.")
        sys.exit(1)

    print(f"Структура директорії {directory}:")
    list_files_and_directories(directory)
