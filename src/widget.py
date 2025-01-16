from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_number: Union[int, str]) -> str:
    """Функция, которая замаскирует счет ИЛИ карту"""
    if "Счет " in str(user_number):
        return get_mask_account(user_number)
    else:
        return get_mask_card_number(user_number)


def get_date(user_date: Union[int, str]) -> str:
    """Функция, которая выводит дату из строки"""
    user_date_update = str(user_date)
    return f"{user_date_update[8:10]}.{user_date_update[5:7]}.{user_date_update[:4]}"


print("Введите номер карты или счета: ")
print(mask_account_card(user_number=input()))
print(get_date(user_date=input()))
