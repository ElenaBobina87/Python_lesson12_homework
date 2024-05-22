from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные? \n \n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    while var != 1 and command != 2:
        print("Неправильный ввод")     # защита от пользователя, если пользователь ввел что-то не то
        var = int(input("Введите число "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")

    if var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")




def print_data():
    print('Вывожу данные из файла data_first_variant: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f: # открывааем файл для вывода данных
        data_first = f.readlines()  # читаем все наши данные
        data_first_list = []  # создаем пустой список для записи итогового результата
        j = 0                 # создаем переменную счетчик
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:  # проверяем, если мы находимся между записями или мы на последней записи о человеке
                data_first_list.append(''.join(data_first[j:i+1])) # если условие выполнено, добавляем запись в список
                j = i
        print(''.join(data_first_list))



    print('Вывожу данные из файла data_second_variant: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:  # открывааем файл для вывода данных
        data_second = f.readlines()  # читаем все наши данные
        # так каз в этом варианте все данные записаны в строку, можно ее просто выводить
        print(*data_second)