# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для
# изменения и удаления данных
import csv
from csv import reader, DictReader
from os.path import exists

def creating():
    file = 'phone.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия,Имя,Номер\n')

def writing_csv(info):
    file = 'phone.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n')

def reading_csv(file):
    # возвращает данные в виде строки
    # with open(file, encoding='utf-8') as data:
    # content = data.read()
    # return content

    # возвращает данные в виде списка
    #with open(file, encoding='utf-8') as data:
        #res = list(reader(data))
    #return res

    with open(file, encoding='utf-8') as data:
        res = list(DictReader(data))
    return res

def get_info():
    info = []
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    # last_name = 'Иванов'
    # first_name = 'Иван'
    info.append(last_name)
    info.append(first_name)
    phone_number = ''
    flag = False
    while not flag:
        try:
            # phone_number = input("Введите номер: ")
            phone_number = '12345678911'
            if len(phone_number) != 11:
                print("В номере должно быть 11 цифр")
            else:
                phone_number = int(phone_number)
                flag = True

        except:
            print("В номере должны быть только цифры")

    info.append(phone_number)
    return info

def record_info():
    info = get_info()
    writing_csv(info)


#record_info()

def view():
    print(reading_csv('phone.csv'))

#view()

def main():
    while True:
        step = input("Введите действие: ")
        if step == 'q':
            break
        elif step == 'w':
            path = 'phone.csv'
            flag = exists(path)
            if not flag:
                creating()
                record_info()
            else:
                record_info()

        elif step == 'r':
            view()



def main():
    while True:
        print("q - Выйти\n r - Просмотреть список\n w - Записать\n d - Удалить\n e - Изменить")
        step = input("Введите действие: ")
        if step == 'q':
            break
        elif step == 'w':
            path = 'phone.csv'
            flag = exists(path)
            if not flag:
                creating()
                record_info()
            else:
                record_info()
        elif step == "d":
            del_cont()
        elif step == "e":
            edit_phone()

        elif step == 'r':
            view()

def edit_phone():
    contact_phone = reading_csv('phone.csv')
    foun_cont = input("Введите фамилию которую хотите отредактировать: ")
    for i in contact_phone:
        if i['Фамилия'] == foun_cont:
            i['Фамилия'] = input("Введите новую фамилию - ")
            i['Имя'] = input("Введите новое Имя - ")
            i['Номер'] = input("Введите новый Номер - ")
    with open('phone.csv', 'w', encoding='utf-8') as f_n:
        F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(contact_phone[0].keys()),
                                    quoting=csv.QUOTE_NONNUMERIC)
        F_N_WRITER.writeheader()
        for d in contact_phone:
            F_N_WRITER.writerow(d)



def del_cont():
    contact_phone = reading_csv('phone.csv')
    foun_cont = input("Введите фамилию которую хотите Удалить -  ")
    for i in contact_phone:
        if i['Фамилия'] == foun_cont:
            del i['Фамилия']
            del i['Имя']
            del i['Номер']

    with open('phone.csv', 'w', encoding='utf-8') as f_n:
        F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(contact_phone[0].keys()),
                                    quoting=csv.QUOTE_NONNUMERIC)

        for d in contact_phone:
            F_N_WRITER.writerow(d)

main()