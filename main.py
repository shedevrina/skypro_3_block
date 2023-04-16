# -*- coding: utf-8 -*-
import json

from functions import operations, data_operations_print

data_client_operations_json = []

with open("operations.json", "r", encoding='utf-8') as file:  # преобразования из файла json в массив
    data_client_operations_json = json.load(file)

executed_operations_last = operations(data_client_operations_json, 5, "EXECUTED")

data_operations_print(executed_operations_last)










