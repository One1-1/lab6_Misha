def task6_1(filename):
    '''
    В файле записана информация о группе людей, содержащая имя и возраст каждого из
    них. Описать процедуру, печатающую имена всех людей из файла, имеющих
    наименьший возраст. Предусмотреть обработку всех возможных исключительных
    ситуаций

    :param filename: имя файла
    :return: None
    '''
    def save_to_file(filename):
        # Функция для сохранения имен и возрастов в файл
        try:
            # Открываем файл для записи
            with open(filename, 'w') as file:
                while True:
                    name = input("Введите имя (или 'exit' для выхода): ")
                    # Проверяем, не ввел ли пользователь 'exit' для выхода
                    if name.lower() == 'exit':
                        break
                    age = input("Введите возраст: ")
                    try:
                        # Пробуем преобразовать возраст в целое число
                        age = int(age)
                        # Записываем имя и возраст в файл
                        file.write(f"{name},{age}\n")
                    except ValueError:
                        # Обрабатываем ошибку, если возраст не является числом
                        print("Ошибка: возраст должен быть числом.")

        except IOError:
            # Обрабатываем ошибку записи в файл
            print("Ошибка при записи в файл.")

    def find_min_age_people(filename):
        # Функция для поиска людей с наименьшим возрастом
        try:
            # Открываем файл для чтения
            with open(filename, 'r') as file:
                people = []  # Список для хранения имен и возрастов
                for line in file:
                    try:
                        # Разбиваем строку на имя и возраст
                        name, age = line.strip().split(',')
                        # Добавляем кортеж (имя, возраст) в список
                        people.append((name, int(age)))
                    except ValueError:
                        # Обрабатываем ошибку, если строка имеет неправильный формат
                        print(f"Ошибка в строке: {line.strip()}. Проверьте формат.")

                # Проверяем, не пуст ли список людей
                if not people:
                    print("Файл пуст.")
                    return

                # Инициализируем минимальный возраст первым значением
                min_age = people[0][1]
                # Находим минимальный возраст среди всех людей
                for person in people:
                    if person[1] < min_age:
                        min_age = person[1]

                # Список для хранения имен людей с минимальным возрастом
                min_age_people = []
                # Собираем имена людей с минимальным возрастом
                for person in people:
                    if person[1] == min_age:
                        min_age_people.append(person[0])

                # Выводим имена людей с наименьшим возрастом
                print("Люди с наименьшим возрастом:")
                for person in min_age_people:
                    print(person)

        except FileNotFoundError:
            # Обрабатываем ошибку, если файл не найден
            print("Ошибка: файл не найден.")
        except IOError:
            # Обрабатываем ошибку чтения файла
            print("Ошибка при чтении файла.")

    save_to_file(filename)  # Сохраняем данные в файл
    find_min_age_people(filename)  # Ищем людей с наименьшим возрастом


def task6_2(filename):
    '''
    Пусть текстовый файл t разбит на непустые строки. Описать функцию count(t, d) для
    подсчета числа строк, которые содержат наибольшее количество заданной буквы d.
    Предусмотреть обработку всех возможных исключительных ситуаций

    :param filename: имя файла
    :return: None
    '''
    def create(filename):
        try:
            # Открываем файл для записи
            with open(filename, 'w', encoding='utf-8') as f:
                print("Введите строки (введите 'STOP' для завершения ввода):")
                while True:
                    # Считываем строку с клавиатуры
                    line = input()
                    # Проверяем, не ввел ли пользователь 'STOP' для завершения ввода
                    if line.strip().upper() == 'STOP':
                        break
                    # Записываем строку в файл, добавляя перевод строки
                    f.write(line + '\n')
        except Exception as e:
            # Обрабатываем любые исключения и выводим сообщение об ошибке
            print(f"Произошла ошибка при создании файла: {e}")
    create(filename)


    def count(filename, d):
        # Проверяем, что d является строкой длиной 1
        if not isinstance(d, str) or len(d) != 1:
            raise ValueError("Параметр d должен быть одной буквой.")

        try:
            # Открываем файл для чтения с кодировкой UTF-8
            with open(filename, 'r', encoding='utf-8') as f:
                # Читаем все строки из файла
                lines = f.readlines()

            max_count = 0  # Переменная для хранения максимального количества вхождений буквы
            max_count_lines = 0  # Переменная для подсчета строк с максимальным количеством вхождений

            # Проходим по каждой строке в файле
            for line in lines:
                # Считаем количество вхождений буквы d в текущей строке
                line_count = line.count(d)
                # Если текущее количество больше максимального, обновляем max_count и сбрасываем счетчик строк
                if line_count > max_count:
                    max_count = line_count
                    max_count_lines = 1
                # Если текущее количество равно максимальному, увеличиваем счетчик строк
                elif line_count == max_count and max_count > 0:
                    max_count_lines += 1

            return max_count_lines  # Возвращаем количество строк с максимальным количеством вхождений
        except FileNotFoundError:
            # Обрабатываем случай, когда файл не найден
            print("Файл не найден.")
            return 0
        except Exception as e:
            # Обрабатываем любые другие исключения и выводим сообщение об ошибке
            print(f"Произошла ошибка: {e}")
            return 0

    letter = input("Введите букву для подсчета: ")  # Запрашиваем у пользователя букву для подсчета
    try:
        result = count(filename, letter)  # Вызываем функцию для подсчета строк
        print(f"Количество строк с наибольшим количеством буквы '{letter}': {result}")  # Выводим результат
    except ValueError as ve:
        # Обрабатываем исключение, если введена неверная буква
        print(ve)











