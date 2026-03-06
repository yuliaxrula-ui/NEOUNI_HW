from datetime import datetime


def get_days_from_today(date_string: str) -> int:
    """
    Обчислює різницю в днях між поточною датою та заданою датою у форматі 'РРРР-ММ-ДД'.

    :param date_string: Рядок з датою у форматі 'YYYY-MM-DD'.
    :return: Кількість днів (int) або None, якщо формат дати невірний.
    """
    try:
        # Перетворення рядка в об'єкт дати
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = datetime.today().date()
        
        # Повертаємо різницю як ціле число
        return (today - given_date).days
    except ValueError:
        return None


if __name__ == "__main__":
    while True:
        user_input = input("Введіть дату (РРРР-ММ-ДД) або 'exit' для виходу: ")
        
        if user_input.strip().lower() == "exit":
            print("Програму завершено. До побачення!")
            break 
            
        result = get_days_from_today(user_input)
        
        if result is not None:
            print(f"Різниця між сьогоднішньою датою та {user_input}: {result} днів.")
        else:
            print("Помилка! Неправильний формат дати. Будь ласка, спробуйте ще раз.")
