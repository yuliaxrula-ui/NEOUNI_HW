import sys
from pathlib import Path

def total_salary(path)->tuple:
    """Обчислення загальної зарплати працівників та середньої зарплати
    """
    total = 0
    count = 0
    
    try:
        with open(path, "r", encoding="utf-8") as salaries:
            for s in salaries:
                try:
                    # Очищаємо рядок від зайвих пробілів та символів \n
                    line = s.strip()
                    if not line: # Пропускаємо порожні рядки, якщо вони є
                        continue
                        
                    developer, salary = line.split(',')
                    salary_value = int(salary)
                    
                    # Додаємо лише якщо зарплата більша за 0
                    if salary_value > 0:
                        total += salary_value
                        count += 1
                except ValueError:
                    # Якщо в рядку немає коми або замість числа — текст
                    print(f"Попередження: Некоректні дані у рядку: {line}")
                    continue

        # Перевіряємо, чи ми знайшли хоча б одного розробника, щоб не ділити на нуль
        if count == 0:
            raise ZeroDivisionError

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return (0, 0)
    except ZeroDivisionError:
        print("Помилка: У файлі немає коректних даних для розрахунку.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася непередбачувана помилка: {e}")
        return (0, 0)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path_to_file = Path(sys.argv[1])
        total, average = total_salary(path_to_file)
        
        if total > 0:
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    else:
        print("Помилка: Ви не вказали шлях до файлу!")
        print("Приклад запуску: python main.py salary_file.txt")
