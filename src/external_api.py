import os

import requests
from dotenv import load_dotenv

from src.utils import all_transaction

load_dotenv()
API_KEY = os.getenv("API_KEY")
transactions = all_transaction("/Users/veronikasidorova/bank_prj/data/operations.json")


def convertion_func(transaction_list: list):  # type: ignore
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount)
    в рублях, тип данных — float. Если транзакция была в USD или EUR, происходит обращение
    к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли"""
    payload = {}  # type: ignore
    headers = {"apikey": API_KEY}
    for transaction in transaction_list:
        from_code = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        if from_code == "RUB":
            yield float(amount)
        else:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_code}&amount={amount}"
            response = requests.request("GET", url, headers=headers, data=payload)
            # status_code = response.status_code
            result = response.json()
            yield float(result.get("result"))


# example = convertion_func(transactions)
# for _ in range(5):
#     print(next(example))
