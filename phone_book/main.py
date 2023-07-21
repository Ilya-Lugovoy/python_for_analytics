from pathlib import Path

FILE_PATH = Path('gb_py', 'phone_book', 'phone_book.txt')
print(FILE_PATH)

def count_id():
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        contact_id = 1
        for line in file:
            contact_id += 1
        return contact_id

def add_contact():
    with open(FILE_PATH, 'a', encoding='utf8') as file:
        info = input('Enter data according to the sample - Last name First name; phone number: ')
        contact_id = count_id()
        file.write(f'\n{contact_id}. {info}')

def show_contact():
    with open(FILE_PATH, 'r', encoding = 'utf8') as file:
        # print([lines for lines in file])
        print(*[line for line in file])
        # print(file.readlines())

def find_contact():
    list_1 = []
    search = input("Enter contact: ").strip()
    with open(FILE_PATH, 'r', encoding = 'utf8') as file:
        for contact in file:
            if search in contact:
                list_1.append(contact)
        print(*(line for line in list_1))

def change_contact():
    show_contact()
    with open(FILE_PATH, 'r+', encoding='utf8') as file:
        n = int(input('Enter a contact number to change it: '))
        lines = file.readlines()
        if n > len(lines):
            print('Invalid contact number')
            return
        new_info = input('Enter data according to the sample - Last name First name; phone number: ')
        lines[n-1] = f'{n}. {new_info}\n'
        file.seek(0)
        file.writelines(lines)

def delete_contact():
    show_contact()
    with open(FILE_PATH, 'r+', encoding='utf8') as file:
        n = int(input('Enter a contact number to delete it: '))
        lines = file.readlines()
        if n > len(lines):
            print('Invalid contact number')
            return
        del lines[n-1]
        file.seek(0)
        file.truncate(0)
        file.writelines(lines)
    
def choose():
    flag=True
    while flag:
        print('Options: \
        1 - add contact \
        2 - show contacts \
        3 - find contact \
        4 - change contact \
        5 - delete contact \
        6 - finish session')
        n = input('Enter option: ')
        match n:
            case '1':
                add_contact()
            case '2':
                show_contact()
            case '3':
                find_contact()
            case '4':
                change_contact()
            case '5':
                delete_contact()
            case '6':
                flag=False

choose()