import json
import os
from datetime import datetime


# путь до папки с данными
DATA_PATH = os.path.join("json_data", "operations.json")


def load_data():
    """
    Загружает выполненные ("EXECUTED") операции из json файла,
    записывает их в список executed_operations и возвращает этот список.
    Если поле "state" не найдено - пропускает.
    :return: executed_operations
    """
    with open(DATA_PATH, "r", encoding="utf-8") as file:

        executed_operations = []
        operations_data = json.load(file)

        for operation in operations_data:

            try:
                if operation["state"] == "EXECUTED":
                    executed_operations.append(operation)

            except KeyError:
                pass

        return executed_operations


def last_operations(data):
    """
    Функция сортирует все выполненные операции по дате (от новой к старой)
    Возвращает последние 5 операций в списке last_excecuted_op
    Изменяет формат даты
    :return: last_excecuted_op
    """
    sorted_list = sorted(data, key=lambda x: x["date"], reverse=True)
    last_excecuted_op = []

    for i in sorted_list:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        i.update(date=date)

    for operation in range(0, 5):
        last_excecuted_op.append(sorted_list[operation])

    return last_excecuted_op


def final_result(data):
    """
    Функция шифрует номера карт и счетов
    выводит отсортированный списко с зашифрованными картами/счетами
    :return:
    """
    final_list = []

    for fd in data:
        date = fd["date"]
        description = fd["description"]
        operation_amount = fd["operationAmount"]["amount"]
        currency = fd["operationAmount"]["currency"]["name"]

        if "from" in fd:
            sent_from = fd["from"].split()
            bill_from = sent_from.pop(-1)
            bill_from = f"{bill_from[:4]} {bill_from[4:6]}** **** {bill_from[-4:]}"
            bill_to = fd["to"].split()
            bill_to = f"{bill_to[0]} **{bill_to[1][-4:]}"
            bill_info = " ".join(sent_from)
            arrow = "->"

        else:
            bill_info = "Открытие вклада"
            bill_from = ""
            bill_to = fd["to"].split()
            bill_to = f"{bill_to[0]} **{bill_to[1][-4:]}"
            arrow = ""

        final_list.append(f"""{date} {description}
{bill_info} {bill_from} {arrow} {bill_to}  
{operation_amount} {currency}\n""")

    return final_list
