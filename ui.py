from logger import input_data, print_data, update_data, delete_data, copy_data


def interface():
    print("Добрый день! Вы попали в бот-справочник от GeekBrains! \n"
          "1 - Запись данных \n"
          "2 - Вывод данных\n"
          "3 - Изменение данных\n"
          "4 - Удаление данных\n"
          "5 - Копирование данных")

    command = int(input('Введите число: '))

    while command not in [1, 2, 3, 4, 5]:
        print("Неправильный ввод")
        command = int(input('Введите число: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        update_data()
    elif command == 4:
        delete_data()
    elif command == 5:
        copy_data()


if __name__ == '__main__':
    interface()
