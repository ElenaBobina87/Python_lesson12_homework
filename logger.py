
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
    while var != 1 and var != 2:
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
    with open('C:/Users/Елена/Desktop/Tel/Python_lesson12_homework/data_first_variant.csv', 'r', encoding='utf-8') as f: # открывааем файл для вывода данных
        data_first = f.readlines()  # читаем все наши данные
        data_first_list = []  # создаем пустой список для записи итогового результата
        j = 0                 # создаем переменную счетчик
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:  # проверяем, если мы находимся между записями или мы на последней записи о человеке
                data_first_list.append(''.join(data_first[j:i+1])) # если условие выполнено, добавляем запись в список
                j = i
        print(''.join(data_first_list))



    print('Вывожу данные из файла data_second_variant: \n')
    with open('C:/Users/Елена/Desktop/Tel/Python_lesson12_homework/data_second_variant.csv', 'r', encoding='utf-8') as f:  # открывааем файл для вывода данных
        data_second = f.readlines()  # читаем все наши данные
        # так каз в этом варианте все данные записаны в строку, можно ее просто выводить
        print(*data_second)

def delete_data():
    
    num = int(input("Введите номер записи, которую хотите удалить "))
    with open('C:/Users/Елена/Desktop/Tel/Python_lesson12_homework/data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_new_list = []  # создаем пустой список для записи итогового результата
        count = 1 # Создаем переменную, которая будет отсчитывать записи (1 запись = 1 человек)
        j = 0                 # создаем переменную счетчик
        for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first)-1:  # проверяем, если мы находимся между записями или мы на последней записи о человеке
                    if count != num: # если запись не равна удаляемой
                        data_first_new_list.append(''.join(data_first[j:i+1])) # если условие выполнено, добавляем запись в список
                    # "этот элс для изменения записи, не для удаления, в функции удаления сразу переходишь на j = i"
                    #else:
                        #data_first_new_list.append(name_data())
                        #data_first_new_list.append(surname_data())
                        #data_first_new_list.append(phone_data())
                        #data_first_new_list.append(address_data())
                        # добавляешь эти 5 строк в функцию удаления и получаешь функцию изменения. Я ее не тестировала, протестируй сама, должно работать, по логике
                    j = i
                    count += 1
        with open('C:/Users/Елена/Desktop/Tel/Python_lesson12_homework/data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write('') # очищаем файл, делаем его пустым
        for i in range(len(data_first_new_list)): # заполняем его заново
            with open('C:/Users/Елена/Desktop/Tel/Python_lesson12_homework/data_first_variant.csv', 'a', encoding='utf-8') as f:
                # открываем файл в режиме дописывания
                new_list = data_first_new_list[i].split('\n') # делаем из списка список, состоящий из маленьких списков (подсписков)
                for k in range(len(new_list)): # для каждого подсписка (подсписок = 1 запись, элемент подсписка = это имя, фамилия, адрес, телефон)
                    if new_list[k] != '': # если элемент не равен пустой строке, а они там есть такие
                        f.write(f"{new_list[k]}\n") # замисываем элемент подсписка в файл
                f.write('\n')
                       
    
    
