from mod_01_hw_10_classes import AddressBook
from mod_01_hw_10_handlers import *

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    # Меню команд для користувача
    print("\nAvailable commands:")
    print("  - Greeting from bot: hello")
    print("  - To close the program: close / exit")
    print("  - To add new contact: add [name] [phone]")
    print("  - To delete contact: delete [name]")
    print("  - To show all contacts: all")
    print("  - To update existing phone: change [name] [old_phone] [new_phone]")
    print("  - To show all phones of a contact: phone [name]")
    print("  - To remove phone: remove [name] [phone]")
    print("  - To add birthday: add-birthday [name] [birthday]")
    print("  - To show birthday: show-birthday [name]")
    print("  - To show all birthdays next week: birthdays\n")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
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
