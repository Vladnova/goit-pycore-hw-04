from typing import List, Tuple, Dict

def parse_input(user_input: str)->Tuple[str, List]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args:Tuple[str, str], contacts:Dict[str, str])->str:
    if len(args) != 2:
        return 'To add a contact, you must enter a name and phone number'

    name, phone = args

    if name in contacts:
        return 'Contact with such names already exists'

    contacts[name] = phone
    return "Contact added!"


def change_contact(args:Tuple[str, str], contacts:Dict[str, str])->str:
    if len(args) != 2:
        return 'To change the contact, you need to enter the name and phone number'

    name, phone= args

    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return f'Contact {name} not found'


def show_phone(args:Tuple[str, str], contacts:Dict[str, str])->str:
    if len(args) != 1:
        return 'Enter only the name of the contact to get the phone number'
    
    name = args[0]

    if name in contacts:
        return contacts[name] 
    else:
        return f'Contact {name} not found'



def show_all(contacts:Dict[str, str])->Dict[str, str] | str:
    if not contacts:
        return 'No contacts added yet'
    return contacts


def main()->str:
    contacts = {}
    print("Welcome to the assistant bot!")


    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))      
        elif command == 'all':
            print(show_all(contacts)) 
        else:
            print('Invalid command.')



if __name__ == "__main__":
    main()