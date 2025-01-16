from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """функция, которая принимает на вход номер карты и возвращает ее маску"""
    card_number_for_mask = str(card_number)
    return f"{card_number_for_mask[:-16]}{card_number_for_mask[-16:-12]} {card_number_for_mask[-12:-14]}** **** {card_number_for_mask[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """функция, которая принимает на вход номер счета и возвращает его маску"""
    account_number_for_mask = str(account_number)
    return f"{account_number_for_mask[:-20]}**{account_number_for_mask[-4:]}"


print("Введите номер карты: ")
print(get_mask_card_number(card_number=input()))
print("Введите номер счета: ")
print(get_mask_account(account_number=input()))
