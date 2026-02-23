from datetime import datetime, timedelta
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
def get_upcoming_birthdays(birthdays):
    b_list=[]
    dt_today=datetime.today().date() #отримуємо сьогоднішню дату один раз
    for b in birthdays: #розпаковуємо список словників
        dt_birthday=datetime.strptime(b["birthday"], "%Y.%m.%d").date().replace(year=dt_today.year) #перетворюємо рядок в дату
        dt_birthday=dt_birthday.replace(year=dt_today.year+1) if dt_birthday<dt_today else dt_birthday #якщо рік менший то додаємо 1 рік 
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
upcoming_birthdays = get_upcoming_birthdays(users)  
print("Список привітань на цьому тижні:", upcoming_birthdays)