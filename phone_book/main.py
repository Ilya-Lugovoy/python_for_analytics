from pathlib import Path

FILE_PATH = Path('gb_py', 'phone_book', 'phone_book.txt')
print(FILE_PATH)

def add_contact():
    with open(FILE_PATH, 'a', encoding = 'utf8') as file:
        info = input('Enter data according to the sample - Last name First name;phone number: ')
        file.write(f'\n{info}')

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
    
def choose():
    flag=True
    while flag:
        print('Options: \
        1 - add contact \
        2 - show contacts \
        3 - find contact')
        n = input('Enter option: ')
        match n:
            case '1':
                add_contact()
                flag = False
            case '2':
                show_contact()
                flag = False
            case '3':
                find_contact()
                flag = False

choose()