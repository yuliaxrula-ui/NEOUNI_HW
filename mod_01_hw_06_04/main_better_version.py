import sys

# --- Функції обробники (Handler) ---

def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Error: Give me name and phone please."
    
    name, phone = args
    name = name.capitalize()
    
    # якщо ім'я вже є, ми нічого не міняємо
    if name in contacts:
        return f"Error: Contact '{name}' already exists. Use 'change' command to update the number."
    
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Error: Give me name and phone please."
    
    name, new_phone = args
    name = name.capitalize()
    
    # Перевірка: чи є кого змінювати
    if name not in contacts:
        return f"Error: Contact '{name}' not found. Use 'add' to create it."
    
    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args: list, contacts: dict) -> str:
    if not args:
        return "Error: Enter user name."
    name = args[0].capitalize()
    return contacts.get(name, "Contact doesn't exist.")

def show_all(contacts: dict) -> dict:
    return contacts

# --- Парсер (Parser) ---

def parse_input(user_input: str):
    if not user_input.strip():
        return "", []
    parts = user_input.strip().split()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

# --- Основна логіка (Main) ---

def show_menu():
    print("\n" + "-"*30)
    print("Commands: hello, add [name] [phone], change [name] [phone], phone [name], all, close, exit")
    print("-"*30)

def main():
    print("Welcome to the assistant bot!")
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
                # Валідація: рівно 2 аргументи та номер з цифр
                if len(args) == 2:
                    if args[1].isdigit():
                        print(add_contact(args, contacts))
                    else:
                        print("Error: Phone number must contain only digits.")
                else:
                    print("Error: Please provide both name and phone.")

            case "change":
                # Валідація: рівно 2 аргументи та номер з цифр
                if len(args) == 2:
                    if args[1].isdigit():
                        print(change_contact(args, contacts))
                    else:
                        print("Error: Phone number must contain only digits.")
                else:
                    print("Error: Please provide both name and phone.")

            case "phone":
                print(show_phone(args, contacts))

            case "all":
                result = show_all(contacts)
                if not result:
                    print("Contact list is empty.")
                else:
                    print("Current contacts:")
                    for name, phone in result.items():
                        print(f"{name}: {phone}")

            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()