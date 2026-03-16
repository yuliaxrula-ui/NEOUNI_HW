from collections import UserDict
from typing import Optional, Iterable
from datetime import datetime, timedelta


class Field:
    """Базовий клас для полів запису."""
    def __init__(self, value: str) -> None:   
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """Клас для зберігання імені контакту. Обов'язкове поле."""
    pass


class Phone(Field):
    """Клас для зберігання номера телефону з валідацією формату."""
    def __init__(self, phone: str) -> None:
        # Перевірка: чи рядок складається лише з цифр і має довжину 10
        if len(phone) == 10 and phone.isdigit():
            super().__init__(phone)
        else:
            raise ValueError("Number must contain 10 digits and no letters.")


class Birthday(Field):
    """Клас для зберігання дня народження з валідацією формату."""
    def __init__(self, birthday: str) -> None:
        try:
            # Зберігаємо одразу як об'єкт datetime.date
            super().__init__(datetime.strptime(birthday, "%d.%m.%Y").date())
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    """Клас для зберігання інформації про контакт (ім'я, телефони, день народження)."""
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Optional[Birthday] = None

    def add_birthday(self, birthday: str) -> None:
        """Додає день народження до контакту."""
        self.birthday = Birthday(birthday)

    def show_birthday(self) -> str:
        """Повертає відформатований день народження або повідомлення про його відсутність."""
        if self.birthday:
            return self.birthday.value.strftime("%d.%m.%Y")
        return "Birthday not added."
    
    def add_phone(self, phone: str) -> None:
        """Додає новий об'єкт Phone до списку телефонів контакту."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """Видаляє телефон зі списку за його рядковим значенням."""
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Шукає старий номер та замінює його на новий."""
        phone_to_update = self.find_phone(old_phone)
        if phone_to_update:
            # Створюємо новий об'єкт Phone для валідації нового номера, 
            # і тільки якщо вона успішна - перезаписуємо значення
            phone_to_update.value = Phone(new_phone).value
        else:
            raise ValueError("Old number not found.")
         
    def find_phone(self, phone: str) -> Optional[Phone]: 
        """Шукає об'єкт Phone за рядковим значенням номера."""
        for p in self.phones:
             if p.value == phone:
                return p
        return None 

    def __str__(self) -> str:
        """Форматує вивід запису для друку в консолі."""
        phones_str = '; '.join(p.value for p in self.phones)
        # Безпечно дістаємо дату, щоб не отримати помилку, якщо дня народження немає
        birthday_str = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "не вказано"
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}"


class AddressBook(UserDict):
    """Клас для зберігання та керування записами (Record)."""
    
    def add_record(self, record: Record) -> None:
        """Додає запис, використовуючи ім'я контакту як ключ."""
        self.data[record.name.value] = record

    def all(self) -> Iterable[Record]:
        """Повертає всі записи з адресної книги."""
        return self.data.values()

    def find(self, name: str) -> Optional[Record]:
        """Повертає запис за іменем або None, якщо не знайдено."""
        return self.data.get(name)
       
    def delete(self, name: str) -> None:
        """Видаляє запис за іменем, якщо такий існує."""
        self.data.pop(name, None)

    def get_upcoming_birthdays(self) -> dict[str, str]:
        """Повертає словник контактів, яких треба привітати в найближчі 7 днів."""
        dt_today = datetime.today().date()
        birthdays = {} 
        
        for record in self.data.values():
            if record.birthday:
                dt_birthday = record.birthday.value
                
                try:
                    dt_birthday = dt_birthday.replace(year=dt_today.year)
                except ValueError:
                    dt_birthday = dt_birthday.replace(year=dt_today.year, month=3, day=1)
                
                if dt_birthday < dt_today:
                    try:
                        dt_birthday = dt_birthday.replace(year=dt_today.year + 1)
                    except ValueError:
                        dt_birthday = dt_birthday.replace(year=dt_today.year + 1, month=3, day=1)
                
                days_until = (dt_birthday - dt_today).days
                
                if 0 <= days_until <= 7:
                    weekday = dt_birthday.weekday()
                    if weekday == 5:  
                        dt_birthday += timedelta(days=2)
                    elif weekday == 6:
                        dt_birthday += timedelta(days=1)
        
                    birthdays[record.name.value] = dt_birthday
                    
        sorted_birthdays_list = sorted(birthdays.items(), key=lambda x: x[1])
        result = {name: date.strftime("%d.%m.%Y") for name, date in sorted_birthdays_list}
                    
        return result