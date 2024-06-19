from csv import DictReader, DictWriter
from os.path import exists
class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            second_name = input('Введите фамилию: ')
            if len(second_name) < 4:
                raise NameError("Слишком короткая фамилия")
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) < 11:
                raise NameError('Слишком короткий номер')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, second_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
    print(f"Файл {file_name} создан.")

def write_file(file_name):
    user_data = get_info()
    res = read_file(file_name)
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    standart_write(file_name, res)
    print(f"Данные записаны в файл {file_name}.")

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r) # список со словарями

def remove_row(file_name):
    search = int(input("Введите строку для удаления: "))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search - 1)
        standart_write(file_name, res)
        print(f"Строка {search} удалена из файла {file_name}.")
    else:
        print('Введен неверный номер строки')

def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)
    print(f"Данные записаны в файл {file_name}.")

def copy_data(src_file, dest_file):
    if not exists(src_file):
        print(f"Файл {src_file} отсутствует.")
        return

    data = read_file(src_file)
    if not data:
        print(f"Файл {src_file} пустой. Нечего копировать.")
        return

    with open(dest_file, 'w', encoding='utf-8', newline='') as data_file:
        f_w = DictWriter(data_file, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(data)
    print(f"Данные скопированы из {src_file} в {dest_file}")

file_name = 'phone.csv'
file_name_1 = 'phone2.csv'

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует, создайте его")
                continue
            print(*read_file(file_name), sep='\n')
        elif command == 'd':
            if not exists(file_name):
                print("Файл отсутствует, создайте его")
                continue
            remove_row(file_name)
        elif command == 'c':
            copy_data(file_name, file_name_1)

main()
