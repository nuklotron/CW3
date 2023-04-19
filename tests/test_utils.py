import json

from utils import load_data, last_operations, final_result


def test_load_data():
    lo_da = load_data()
    #загружаю ожидаемый результат от функции load_data() для сравнения
    test_list = []
    with open("tests/json_data/operations.json", encoding="utf-8") as f:
        test_data = json.load(f)
        for k in test_data:
            test_list.append(k)

    assert lo_da == test_list


def test_last_operations(test_data):
    l_op = last_operations(test_data)
    assert [x["date"] for x in l_op] == ["08.12.2019", "07.12.2019", "19.11.2019", "13.11.2019", "05.11.2019"]


def test_final_result(test_data):
    l_op = last_operations(test_data)
    f_re = final_result(l_op)
    assert f_re == ['08.12.2019 Открытие вклада\nОткрытие вклада   Счет **5907  \n41096.24 USD\n', '07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655  \n48150.39 USD\n', '19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869  \n30153.72 руб.\n', '13.11.2019 Перевод со счета на счет\nСчет 3861 14** **** 9794 -> Счет **8125  \n62814.53 руб.\n', '05.11.2019 Открытие вклада\nОткрытие вклада   Счет **8381  \n21344.35 руб.\n']
