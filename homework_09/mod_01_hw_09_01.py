from collections import UserDict
from typing import Optional

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
            raise ValueError("Номер повинен містити 10 цифр і жодної букви")
        

class Record:
    """Клас для зберігання інформації про контакт (ім'я та список телефонів)."""
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []

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
            raise ValueError("Старий номер не знайдено")
         
    def find_phone(self, phone: str) -> Optional[Phone]: 
        """Шукає об'єкт Phone за рядковим значенням номера."""
        for p in self.phones:
             if p.value == phone:
                return p
        return None

    def __str__(self) -> str:
        # Форматуємо вивід запису
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    """Клас для зберігання та керування записами (Record)."""
    def add_record(self, record: Record) -> None:
        """Додає запис, використовуючи ім'я контакту як ключ."""
        self.data[record.name.value] = record
   
    def find(self, name: str) -> Optional[Record]:
        """Повертає запис за іменем або None, якщо не знайдено."""
        return self.data.get(name)
       
    def delete(self, name: str) -> None:
        """Видаляє запис за іменем, якщо такий існує."""
        self.data.pop(name, None)