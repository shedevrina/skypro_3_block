import pytest

from functions import operations, data_operations_print


@pytest.fixture()

def сoll_function(): #фикстура

    test_list = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'NOT', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]
    return test_list, 2, 'EXECUTED'

def test_data_operations(сoll_function):

    assert operations(сoll_function[0], сoll_function[1], сoll_function[2]) == {'id': 863064926, 'state': 'EXECUTED', 'date': '08.12.2019', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'from': 'Maestro 159 6** **** 5199','to': 'Счет **9589'}

def test_data_operations_print():

    assert data_operations_print