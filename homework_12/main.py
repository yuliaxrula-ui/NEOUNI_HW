import pickle
from classes import AddressBook
from handlers import *

def save_data(book, filename="addressbook.pkl"):
    """
    Серіалізує об'єкт AddressBook у файл за допомогою pickle.
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """
    Десеріалізує дані з файлу. Якщо файл не знайдено, 
    створює нову порожню книгу.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook() 

def main():
    # Відновлення стану при запуску програми
    book = load_data()
    
    print("Welcome to the assistant bot!")
    print("\nAvailable commands: hello, add, delete, all, change, phone, remove, add-birthday, show-birthday, birthdays, close/exit\n")

    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue
            
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            # Збереження стану при закритті програми
            save_data(book)
            print("Good bye! All your contacts are saved.")
            break
            
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(handle_add_contact(args, book))
        elif command == "remove":
            print(handle_remove_phone(args, book))
        elif command == "change":
            print(handle_change_phone(args, book))
        elif command == "delete":
            print(handle_delete_contact(args, book))
        elif command == "phone":
            print(handle_find(args, book))
        elif command == "all":
            print(handle_all(book))
        elif command == "add-birthday":
            print(handle_add_birthday(args, book))
        elif command == "show-birthday":
            print(handle_show_birthday(args, book))
        elif command == "birthdays":
            print(handle_get_upcoming_birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
