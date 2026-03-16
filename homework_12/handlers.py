from classes import AddressBook, Record
from decorators import input_error

def parse_input(user_input: str) -> tuple[str, ...]:
    """
    Парсить введений користувачем рядок.
    Повертає команду (перше слово в нижньому регістрі) 
    та список аргументів (усі інші слова).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def handle_add_contact(args: list[str], book: AddressBook) -> str:
    """Додає новий контакт або новий телефон до існуючого контакту."""
    name, phone, *_ = args
    record = book.find(name)
    
    # Заготовка повідомлення (якщо контакт вже є)
    message = "Contact updated."
    
    # Якщо контакту немає, створюємо його і змінюємо повідомлення
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
        
    # Додаємо телефон
    if phone:
        record.add_phone(phone)
        
    return message

@input_error
def handle_change_phone(args: list[str], book: AddressBook) -> str:
    """Змінює старий телефон на новий для вказаного контакту."""
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    
    if record is None:
        return "Contact not found."
        
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."

@input_error
def handle_remove_phone(args: list[str], book: AddressBook) -> str:
    """Видаляє вказаний телефон у контакту."""
    name, phone, *_ = args
    record = book.find(name)
    
    if record is None:
        return "Contact not found."
        
    # Передаємо в метод класу ТІЛЬКИ телефон (як ми і прописали в Record)
    record.remove_phone(phone)
    return "Phone removed."

@input_error
def handle_delete_contact(args: list[str], book: AddressBook) -> str:
    """Видаляє контакт з адресної книги повністю."""
    name, *_ = args
    record = book.find(name)
    
    if record is None:
        return "Contact not found."
        
    book.delete(name)
    return "Contact deleted."

@input_error
def handle_find(args: list[str], book: AddressBook) -> str:
    """Повертає інформацію про вказаний контакт (для команди phone)."""
    name, *_ = args
    record = book.find(name)
    
    if record is None:
        return "Contact not found."
        
    # Метод __str__ у класі Record
    return str(record)

@input_error
def handle_all(book: AddressBook) -> str:
    """Повертає рядок з усіма контактами в адресній книзі."""
    if not book.data:
        return "Address book is empty."
        
    # Проходимося по всіх записах і об'єднуємо їх у великий текст (кожен з нового рядка)
    records_list = [str(record) for record in book.all()]
    return "\n".join(records_list)

@input_error
def handle_add_contact(args: list[str], book: AddressBook) -> str:
    """Додає новий контакт або новий телефон до існуючого контакту."""
    name, phone, *_ = args
    
    # 1. Спочатку валідуємо телефон, створюючи об'єкт Phone.
    # Якщо формат невірний, виникне ValueError і функція перерветься тут.
    new_phone_obj = Phone(phone) 
    
    record = book.find(name)
    message = "Contact updated."
    
    if record is None:
        # 2. Тільки якщо телефон валідний, створюємо Record
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
        
    # Додаємо вже провалідований телефон
    record.phones.append(new_phone_obj)
        
    return message

@input_error
def handle_show_birthday(args: list[str], book: AddressBook) -> str:
    """Показує день народження вказаного контакту."""
    name, *_ = args
    record = book.find(name)
    
    if record is None:
        return "Contact not found."
        
    return str(record.show_birthday())

@input_error
def handle_get_upcoming_birthdays(book: AddressBook) -> str:
    """Показує дні народження, які відбудуться протягом наступного тижня."""
    birthdays = book.get_upcoming_birthdays()
    
    if not birthdays:
        return "No birthdays next week."
        
    # Форматуємо словник у красивий текстовий список для виводу в консоль
    result = ["Birthdays next week:"]
    for name, date in birthdays.items():
        result.append(f"{name}: {date}")
        
    return "\n".join(result)