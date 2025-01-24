from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """функция, которая принимает на вход номер карты и возвращает ее маску"""
    card_number_for_mask = str(card_number)
    if len(card_number_for_mask) == 16 and card_number_for_mask.isdigit():
        return f"{card_number_for_mask[0:4]} " f"{card_number_for_mask[4:6]}** **** " f"{card_number_for_mask[-4:]}"
    else:
        return "Введены некорректные данные"


def get_mask_account(account_number: Union[int, str]) -> str:
    """функция, которая принимает на вход номер счета и возвращает его маску"""
    account_number_for_mask = str(account_number)
    if len(account_number_for_mask) == 20 and account_number_for_mask.isdigit():
        return f"**{account_number_for_mask[-4:]}"
    else:
        return "Введены некорректные данные"


# print("Введите номер карты: ")
# print(get_mask_card_number(card_number=input()))
# print("Введите номер счета: ")
# print(get_mask_account(account_number=input()))
