from logger import input_data, print_data


def interface():
    print('Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1-запись данных \n 2-вывод данных')  #с помощью \n осуществляется переход на новую строку
    command = int(input("Введите число "))    #создаем переменную, которая будет принимать данные с консоли
    while command != 1 and command != 2:
        print("Неправильный ввод")     # защита от пользователя, если пользователь ввел что-то не то
        command = int(input("Введите число "))

    if command ==1:
        input_data()
    elif command ==2:
        print_data()