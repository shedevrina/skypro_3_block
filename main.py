# -*- coding: utf-8 -*-

if __name__ == "__main__":

    from functions import data_json, operations, data_operations_print

    data_client_operations_json = []

    data = data_json("operations.json")

    executed_operations_last = operations(data, 5, "EXECUTED")

    data_operations_print(executed_operations_last)










