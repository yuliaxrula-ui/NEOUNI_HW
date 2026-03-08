from typing import Callable, Dict, List, Tuple


# --- Декоратор для обробки логічних помилок ---
def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            # Текст помилки в raise ValueError("текст") виведеться тут
            if str(e):
                return str(e)
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name or phone please."
    return inner


# --- Обробка команд ---
@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Додає новий контакт. Перевіряє, щоб номер складався лише з цифр."""
    name, phone = args
    name = name.capitalize()
    
    # Специфічна перевірка: номер має бути цифровим
    if not phone.isdigit():
        raise ValueError("Error: Phone number must contain only digits.")
    
    if name in contacts:
        return f"Contact '{name}' already exists. Use 'change' to update."
    
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Змінює існуючий контакт."""
    name, new_phone = args
    name = name.capitalize()

    if name not in contacts:
        raise KeyError
    
    if not new_phone.isdigit():
        raise ValueError("Error: New phone number must contain only digits.")
        
    contacts[name] = new_phone
    return "Contact updated."


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Повертає номер телефону за ім'ям."""
    name = args[0].capitalize()
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts: Dict[str, str]) -> Dict[str, str]:
    """Повертає копію словника контактів за допомогою Dictionary Comprehension"""
    if not contacts:
        raise ValueError("Contact list is empty.")
    
    return {name: phone for name, phone in contacts.items()}


# --- Парсер ---
def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Обробляє ввід від користувача і повертає кортеж зі значенням команди та списком аргументів."""
    if not user_input.strip():
        return "", []
    parts = user_input.strip().split()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


# --- Головна функція взаємодії з користувачем ---
def main():
    print("Welcome to the assistant bot!")
    
    # Повертаємо меню команд для користувача
    print("\nAvailable commands:")
    print("  - hello: Greeting from bot")
    print("  - add [name] [phone]: Add new contact")
    print("  - change [name] [phone]: Update existing phone")
    print("  - phone [name]: Show phone for contact")
    print("  - all: Show all contacts")
    print("  - close / exit: Close the program\n")

    contacts = {}  
    
    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                result = show_all(contacts)
                # Перевірка типу результату (словник або рядок з помилкою)
                if isinstance(result, dict):
                    print("Current contacts:")
                    for name, phone in result.items():
                        print(f"{name}: {phone}")
                else:
                    print(result) # Виведе текст помилки з ValueError
            case _:
                print("Invalid command. Available: hello, add, change, phone, all, exit.")


if __name__ == "__main__":
    main()