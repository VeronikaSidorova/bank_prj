from typing import Any

import pandas as pd

file_on_csv = "/Users/veronikasidorova/bank_prj/data/transactions.csv"
file_on_excel = "/Users/veronikasidorova/bank_prj/data/transactions_excel.xlsx"


def reader_csv(file_csv: Any) -> list[dict]:
    """Функция для считывания финансовых операций из CSV принимает путь
    к файлу CSV в качестве аргумента и выдает список словарей с транзакциями."""
    transactions_from_csv = pd.read_csv(file_csv)
    transactions_from_csv_list = transactions_from_csv.to_dict(orient="records")
    return transactions_from_csv_list


# print(reader_csv(file_on_csv))


def reader_excel(file_excel: Any) -> list[dict]:
    """Функция для считывания финансовых операций из Excel принимает путь
    к файлу Excel в качестве аргумента и выдает список словарей с транзакциями"""
    transactions_from_excel = pd.read_excel(file_excel)
    transactions_from_excel_list = transactions_from_excel.to_dict(orient="records")
    return transactions_from_excel_list


# print(reader_excel(file_on_excel))
