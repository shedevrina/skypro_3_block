# -*- coding: utf-8 -*-

import json
import datetime

def data_operations(data_json, num_last_transactions, status_name, executed_operations=[]):
    """Функция data_operations выводит на экран список из 5 последних выполненных клиентом операций в формате:

<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>

На вход подается база транзакций json, количество операций для вывода на экран, статус нужных операций.
В случае успеха, функция возвращает True."""

    def state_sort(operations, status_name):
        """Функция state_sort - вложеная для функции data_operations. Отбирает транзакции по статусу.
    """
        for data_client_operation in operations:  # фильтр по EXECUTED транзакциям

            if 'state' in data_client_operation:

                if data_client_operation['state'] == status_name:
                    executed_operations.append(data_client_operation)

            else:
                continue
        return executed_operations

    def pic_from(user_one_operation):
        """Функция pic_from - вложеная для функции data_operations. Форматирует вывод значения по ключу 'from'.
    """
        if 'from' in user_one_operation:
            massive_from = user_one_operation['from'].split(' ')
            massive_from[-1] = massive_from[-1][:3] + " " + massive_from[-1][4:5] + "**" + " " + "****" + massive_from[-1][-4:]
            user_one_operation['from'] = ' '.join(massive_from)
        else:
            user_one_operation['from'] = 'Не возможно установить номер счёта'

        return user_one_operation['from']

    def pic_to(user_one_operation):
        """Функция pic_to - вложеная для функции data_operations. Форматирует вывод данных по ключу 'to'.
    """
        if 'to' in user_one_operation:
            massive_to = user_one_operation['to'].split(' ')
            massive_to[-1] = "**" + massive_to[-1][-4:]
            user_one_operation['to'] = ' '.join(massive_to)
        else:
            user_one_operation['to'] = 'Не возможно установить номер счёта'

        return user_one_operation['to']


    with open(data_json, "r", encoding='utf-8') as file: #преобразования из файла json в массив
        data_client_operations = json.load(file)

    sort_massive_state = state_sort(data_client_operations, status_name) #сортировка по 'state'

    executed_operations.sort(key=lambda dictionary: dictionary['date']) #сортировка по 'date'

    for one_operation_last in sort_massive_state[-num_last_transactions:]: #преобразование значени по ключу 'date' строка -> datatime

        if 'date' in one_operation_last:
            one_operation_last['date'] = datetime.datetime.strptime(one_operation_last['date'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            continue

    my_new_list = list(reversed(sort_massive_state[-num_last_transactions:])) #реверс списка

    for one_operation in my_new_list: #вывод print транзакций в нужном формате
        print(f'''{one_operation['date'].strftime('%d.%m.%Y')} {one_operation['description']}
    {pic_from(one_operation)} -> {pic_to(one_operation)}
    {one_operation['operationAmount']['amount']} {one_operation['operationAmount']['currency']['name']}
    ''')

    return True