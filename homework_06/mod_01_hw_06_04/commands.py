def add_contact(args: list, contacts: dict)->dict:
    name, phone = args
    name = name.capitalize()
    # Перевіряємо, чи ключ (ім'я) вже є у словнику
    if name in contacts:
        return f"Error: Contact '{name}' already exists with phone {contacts[name]}."
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list, contacts: dict)->dict:
    name, new_phone = args
    name = name.capitalize()
    if name not in contacts:
        return f"Error: Contact '{name}' doesn't exist."
    contacts.update({name: new_phone})
    return "Contact updated"

def show_phone(args: list, contacts: dict)->dict:
   name = args[0]
   return contacts.get(name.capitalize(),"Contact doesn't exist")

def show_all(contacts: dict)->dict:
    return contacts
    
