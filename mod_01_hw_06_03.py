import sys
from pathlib import Path
from colorama import Fore, init

# Скидання кольору після кожного print
init(autoreset=True)

# Список папок, які ми не хочемо бачити
IGNORE_LIST = {".venv", ".vscode", "__pycache__", ".git"}

def colored_files(path_par, indent=""):
    """Зафарбовує в різні кольори папки та файли та створює деревоподібну структуру"""
    base_path = Path(path_par)
    
    # Перевірка на старті
    if not base_path.exists() or not base_path.is_dir():
        print(f"{Fore.RED}Вказаний шлях не є директорією")
        return

    # Сортуємо: спочатку папки, потім файли
    items = sorted(base_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

    for el in items:
        # Перевірка: якщо назва папки в списку ігнору — пропускаємо
        if el.name in IGNORE_LIST or el.name.startswith('.'):
            continue

        if el.is_dir():
            # Виводимо папку синім
            print(f"{indent}{Fore.BLUE}{el.name}/")
            # Йдемо вглиб (рекурсія)
            colored_files(el, indent + "    ")
        else:
            # Виводимо файл фіолетовим (Magenta)
            print(f"{indent}{Fore.MAGENTA}{el.name}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Викликаємо функцію для шляху з аргументів
        colored_files(sys.argv[1])
    else:
        # Якщо аргумент не вказано, показуємо поточну папку
        colored_files(".")
 