import re
from commands import *
from parser import *

def show_menu():
    print("\n-----Available commands-----")
    print("Hello")
    print("Add <Name> <Phone>")
    print("Change <Name> <New Phone>")
    print("All")
    print("Phone <Name>")
    print("Exit or Close")

def main():
    print("Welcome to the assistant bot!")
    contacts={}
    while True:
        show_menu()
        user_input = input("Enter a command: ")
        pattern=r"^((add|change)\s+(\w+)\s+(\d+)|hello|close|exit|all|phone\s+(\w+))$"

        if re.search(pattern,user_input,flags=re.IGNORECASE)!=None:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(add_contact(args,contacts))

            elif command == "change":
                print(change_contact(args,contacts))
    
            elif command == "all":
                contacts_list = show_all(contacts) # Отримуємо словник
                for name, phone in contacts_list.items():
                    print(f"{name}: {phone}")

            elif command == "phone":
                print(show_phone(args,contacts))

        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()