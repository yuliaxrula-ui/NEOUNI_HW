from datetime import datetime, timedelta


def get_upcoming_birthdays(birthdays: list)->list:
    """
    Повертає список користувачів, яких потрібно привітати протягом наступних 7 днів.
    Якщо ДН у вихідні, дата привітання переноситься на понеділок.
    Обробляє 29 лютого для не високосних років.
    """
    b_list=[]
    dt_today=datetime.today().date() #Отримуємо сьогоднішню дату один раз


    for b in birthdays: #Розпаковуємо список словників
        dt_birthday=datetime.strptime(b["birthday"], "%Y.%m.%d").date() #Перетворюємо рядок в дату

        try:
            dt_birthday=dt_birthday.replace(year=dt_today.year) #Намагаємося підставити поточний рік
        except ValueError:
            # Якщо 29 лютого не існує в цьому році, переносимо на 1 березня
            dt_birthday = dt_birthday.replace(year=dt_today.year, month=3, day=1)

        if dt_birthday < dt_today:
            try:
                dt_birthday = dt_birthday.replace(year=dt_today.year + 1) #Якщо дн минув, переносимо на наступний рік
            except ValueError:
                dt_birthday = dt_birthday.replace(year=dt_today.year + 1, month=3, day=1)
                
        days_until = (dt_birthday - dt_today).days
        if 0 <= days_until <= 7:
            congratulation_date=dt_birthday
            weekday = congratulation_date.weekday()
            if weekday == 5:  
                congratulation_date += timedelta(days=2)
            elif weekday == 6: 
                congratulation_date += timedelta(days=1)
            b_list.append({"name": birthdays["name"],"congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    return b_list

if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)  
    print("Список привітань на цьому тижні:", upcoming_birthdays)