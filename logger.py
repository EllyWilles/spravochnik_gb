from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число'))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.read()
        print(data_first)

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.read()
        print(data_second)


def update_data():
    name_or_surname = input("Введите имя или фамилию для обновления: ")
    new_name = name_data()
    new_surname = surname_data()
    new_phone = phone_data()
    new_address = address_data()
    var = int(input("Выберите файл для обновления данных\n"
                    "1 - data_first_variant.csv\n"
                    "2 - data_second_variant.csv\n"
                    "Введите число: "))

    while var not in [1, 2]:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        file_name = 'data_first_variant.csv'
    else:
        file_name = 'data_second_variant.csv'

    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    updated = False
    new_lines = []

    if var == 1:
        i = 0
        while i < len(lines):
            if lines[i].strip() == name_or_surname or lines[i + 1].strip() == name_or_surname:
                new_lines.extend([f"{new_name}\n", f"{new_surname}\n", f"{new_phone}\n", f"{new_address}\n", "\n"])
                updated = True
                i += 5  # Пропустить следующую запись
            else:
                new_lines.extend(lines[i:i + 5])
                i += 5
    else:
        delimiter = ';'
        for line in lines:
            parts = line.strip().split(delimiter)
            if parts[0] == name_or_surname or parts[1] == name_or_surname:
                new_lines.append(f"{new_name};{new_surname};{new_phone};{new_address}\n")
                updated = True
            else:
                new_lines.append(line)

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    if updated:
        print("Данные успешно обновлены")
    else:
        print("Запись не найдена")



def delete_data():
    name_or_surname = input("Введите имя или фамилию для удаления: ")
    var = int(input("Выберите файл для удаления данных\n"
                    "1 - data_first_variant.csv\n"
                    "2 - data_second_variant.csv\n"
                    "Введите число: "))

    while var not in [1, 2]:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        file_name = 'data_first_variant.csv'
    else:
        file_name = 'data_second_variant.csv'

    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(0, len(lines), 5 if var == 1 else 1):
            if not (lines[i].strip() == name_or_surname or
                    lines[i + 1].strip() == name_or_surname if var == 1 else lines[i].split(';')[1] == name_or_surname):
                f.writelines(lines[i:i + (5 if var == 1 else 1)])


def copy_data():
    var_from = int(input("Из какого файла копировать данные\n"
                         "1 - data_first_variant.csv\n"
                         "2 - data_second_variant.csv\n"
                         "Введите число: "))

    while var_from not in [1, 2]:
        print("Неправильный ввод")
        var_from = int(input('Введите число: '))

    var_to = 2 if var_from == 1 else 1
    file_from = 'data_first_variant.csv' if var_from == 1 else 'data_second_variant.csv'
    file_to = 'data_second_variant.csv' if var_from == 1 else 'data_first_variant.csv'

    line_number = int(input("Введите номер строки для копирования: "))

    with open(file_from, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data_to_copy = lines[line_number - 1].strip()

    if var_from == 1:
        data_to_copy = data_to_copy.replace('\n', ';')

    with open(file_to, 'a', encoding='utf-8') as f:
        if var_to == 1:
            f.write(data_to_copy.replace(';', '\n') + '\n\n')
        else:
            f.write(data_to_copy + '\n')
