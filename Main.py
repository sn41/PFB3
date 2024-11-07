from time import sleep


# Очистить экран
def my_clear_screen():
    for i in range(70):
        print("\n")


# Задержка. delay - в секундах!
def my_sleep(delay):
    sleep(delay)


# Преобразует число в строку.
def my_get_delay_tip_string(delay_tip):
    # Последовательно сравниваем delay_tip со значениями
    # 1, 2, 3
    # если delay_tip и значение совпали - выполняем соответствующий блок кода
    # и выходим из оператора match.
    # Например, если delay_tip равно 1, выполнится delay_tip_string = "- Один!"

    # Если ни один из вариантов не совпал с  delay_tip,
    # тогда выполняется блок кода по-умолчанию
    #   case _:
    # Здесь, это -
    #   delay_tip_string = "- Дальше не умею считать..."

    match delay_tip:
        case 1:
            delay_tip_string = "- Один!"
        case 2:
            delay_tip_string = "- Два!"
        case 3:
            delay_tip_string = "- Три!"
        case _:
            delay_tip_string = "- Дальше не умею считать..."

    # Выходим из функции и возвращаем delay_tip_string
    return delay_tip_string


# Читаем значение, ввёдёное с консоли.
def my_read_console():
    # Строка введённая пользователем.
    str = input()
    # Преобразуем строку в число, возвращаем.
    return int(str)


# Читаем ответ введёный с клавиатуры
# Приводим число к диапазону 1-3,
    # Читаем число введёное с консоли, используя нашу функцию  my_read_console()
    # Приводим прочитанное число к диапазону 1-3
    # Если answer_int меньше двух - ответ будет 1
    # Если answer_int равен двум - ответ будет 2
    # Иначе ответ будет 3
    # elif это - else if
def my_get_answer():
    answer_int = my_read_console()
    if answer_int < 2:
        answer = 1
    elif answer_int == 2:
        answer = 2
    else:
        answer = 3
    return answer


# Используемые значения - константы
FIELD = 10.58
NAME1 = "Вася"
NAME2 = "Джин"
TIME1 = 10
SPEED = 100.0
AGREEMENT = False
AGREEMENT_STRING1 = "- Ну, я пошёл..."
AGREEMENT_STRING2 = "- Счас, разбежался! Сам сгинь!"

# Определяем главный метод
def main():
    # Используем строки с форматированием - f перед строкой
    print(f"{NAME1}: - Который час? Я тебя {TIME1} раз спрашиваю!")
    print(f"{NAME2}: - Сейчас  {FIELD}! Я тебе {TIME1} раз отвечаю!")
    print(f"{NAME1} - Сгинь со скоростью {SPEED} километров в час!")

    # Получить строку ответа, для AGREEMENT = False, это AGREEMENT_STRING2 = "- Счас, разбежался! Сам сгинь!"
    if AGREEMENT:
        agreement_string = AGREEMENT_STRING1
    else:
        agreement_string = AGREEMENT_STRING2

    # Выводим строку "- Счас, разбежался! Сам сгинь!"
    print(agreement_string)

    print("- Сгинь, пропади!")

    # Три раза "Тьфу!" через левое плечо.
    for i in range(3):
        print("- Тьфу!")

    # Выводим вопрос -
    #   читаем консоль -
    #       по введённому значению находим строку ответа -
    #           выводим эту строку

    # list ответов
    sentences = ["Нифига!", "Ни за что!", "Никогда!"]
    # Вывести вопрос на экран - на экран консоли.
    print(NAME2 + ":- У меня есть три ответа, выбери, какой ты хочешь услышать?")
    # Получить ответ с клавиатуры - с консоли, используя написанную нами функцию my_get_answer()
    #   Она возвращает значение 1 или 2 или 3
    #       а индексы значений списка sentences равны 0,1,2
    #           поэтому приводим диапазон ответов к диапазону индексов, отнимаем 1.
    answer_index = my_get_answer() - 1
    # Получаем строку ответа, читаем элемент списка sentences по его индексу answer_index
    answer_string = sentences[answer_index]
    # Печатаем строку ответа
    print(NAME2 + ":- Вот тебе ответ - " + answer_string)

    # Пустые строки
    print("\n\n")

    print(NAME1 + ": - Считаю!!!\n")

    # Заполняем list отсчётов
    # Там будет {0,1,2,3,4,5,6,7,8,9,10}
    delay_tips = []

    for i in range(11):
        delay_tips.append(i)

    # Чтобы прочитать весь список,
    #  начиная с элемента с индексом 1,
    #   до элемента с индексом 10,
    #    с шагом в 1 элемент,
    #     мы используем  диапазон - range.
    #
    # Он задаётся параметрами:
    # - start_included - первый элемент диапазона, включительно
    # - stop_not_included - элемент, перед котором остановится перебор значений,
    # - step_incrementation - шаг перебора значений.
    # range(start_included, stop_not_included, step_incrementation)
    delay_tips_range = range(1, 11, 1)

    # Выполняем цикл -
    #   получаем число из списка - delay_tip
    #       преобразуем число delay_tip в строку функцией my_get_delay_tip_string(delay_tip)
    #               результат помещаем в переменную delay_tip_string
    #           выводим на экран эту строку print(delay_tip_string),
    #       ждём две секунды
    #    проверяем, содержалась ли строка "умею" в выведеной на экран строке delay_tip_string
    #    если содержалась - прекращаем цикл, иначе - переходим к следующей итерации цикла
    #
    # Другими словами, выводим строки на экран, пока мы не прочитаем все значения списка,
    #   соответствующие delay_tips_range
    #       или в выводимой строке не появится слово "умею"

    for i in delay_tips_range:

        delay_tip = delay_tips[i]
        delay_tip_string = my_get_delay_tip_string(delay_tip)
        print(delay_tip_string)

        # задержка в секундах!
        my_sleep(2)
        if "умею" in delay_tip_string:
            break

    # Пауза 2 секунды
    my_sleep(2)

    print(NAME2 + ": - О! Как ты мне надоел. Улетаю, шут с тобой!")

    # Пауза 2 секунды
    my_sleep(3)

    # Очистить экран
    my_clear_screen()


# Мы описали функции и переменные, теперь запустим программу.
main()
