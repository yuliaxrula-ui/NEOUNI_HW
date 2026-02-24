#завдання 1
from datetime import datetime
def get_days_from_today(date_string):
    try:
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - given_date).days
    except ValueError:
        return None
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
