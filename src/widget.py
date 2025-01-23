from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_number: Union[str]) -> str:
    """Функция, которая замаскирует счет ИЛИ карту"""
    if user_number.lower().startswith('счет'):
        account_number = user_number[-20:]
        return f"{user_number[:-20]}{get_mask_account(account_number)}"
    else:
        card_number = user_number[-16:]
        return f"{user_number[:-16]}{get_mask_card_number(card_number)}"


def get_date(user_date: Union[str]) -> str:
    """Функция, которая выводит дату из строки"""
    user_date_update = str(user_date)
    return f"{user_date_update[8:10]}.{user_date_update[5:7]}.{user_date_update[:4]}"


print("Введите номер карты или счета: ")
print(mask_account_card(user_number=input()))
print(get_date(user_date=input()))
