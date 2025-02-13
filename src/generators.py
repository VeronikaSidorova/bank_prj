from typing import Iterator


def filter_by_currency(transactions: list, currency_code: str) -> Iterator:
    """Функция, которая принимает на вход список словарей, представляющих
    транзакции и возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator:
    """Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генератор может сгенерировать номера карт в
    заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    zero_number = "0000000000000000"
    for number in range(start, stop + 1):
        if start < 0:
            yield "Некорректное значение"
            break
        else:
            new_card_number = str(f"{zero_number[:-len(str(number))]}{number}")
            if len(str(new_card_number)) == 16:
                yield f"{new_card_number[:4]} {new_card_number[4:8]} {new_card_number[8:12]} {new_card_number[12:]}"
            else:
                if stop > 9999999999999999:
                    yield "Некорректное значение"
                    break


# example_transactions = (
#     [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160"
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {
#                 "amount": "56883.54",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229"
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657"
#         }
#     ]
# )

# for card_number in card_number_generator(3, 5):
#     print(card_number)

# usd_transactions = filter_by_currency(example_transactions, "USD")
# rub_transactions = filter_by_currency(example_transactions, "RUB")
# a = filter_by_currency(example_transactions, "")
# for _ in range(2):
# print(next(usd_transactions))
# print(next(rub_transactions))
# print(next(a))

# example_descriptions = transaction_descriptions(example_transactions)
# for _ in range(5):
#     print(next(example_descriptions))
