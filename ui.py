from logger import input_data, print_data, delete_data


def interface():
    print('Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1-запись данных \n 2-вывод данных \n 3-удаление данных')  #с помощью \n осуществляется переход на новую строку
    command = int(input("Введите число "))    #создаем переменную, которая будет принимать данные с консоли
    while command != 1 and command != 2 and command != 3:
        print("Неправильный ввод")     # защита от пользователя, если пользователь ввел что-то не то
        command = int(input("Введите число "))

    if command ==1:
        input_data()
    elif command ==2:
        print_data()
    elif command ==3:
        print_data() # распечатываем справочник, чтобы выбрать запись, которую надо удалить.
        # Было бы гораздо удобней и проще, если бы записи нумеровались, например 1.1, 1.2 и 2.1 и 2.2 и тд
        # Далее надо запросить, в каком из файлов будем удалять запись и в зависимости от выбора файла выбрать функцию
        # Данная функция содержится в файле logger и удаляет из первого файла. На ее основе можно сделать для второго
        delete_data()