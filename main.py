"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивае"""


from lab6.my_library import task6_1, task6_2


def menu():
    """
    Функция предлагает выбор номера задания и номера лабораторной работы\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
             choice_lab - выбранный номер лабы
    """
    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()
        print('программа запустилась')


        match choice:

            case 1:

                task6_1(filename='people.txt')

            case 2:

                filename = 'input.txt'
                task6_2(filename)


            case _:
                break

        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

