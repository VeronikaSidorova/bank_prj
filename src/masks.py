import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("/Users/veronikasidorova/bank_prj/logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """функция, которая принимает на вход номер карты и возвращает ее маску"""
    logger.info(f"Запрашиваем номер карты для маскировки {card_number}")
    card_number_for_mask = str(card_number)
    if len(card_number_for_mask) == 16 and card_number_for_mask.isdigit():
        logger.info("Маскируем номер карты")
        return f"{card_number_for_mask[0:4]} " f"{card_number_for_mask[4:6]}** **** " f"{card_number_for_mask[-4:]}"
    else:
        if card_number_for_mask == "":
            logger.info("Если номер карты пустой возвращаем пустую строку")
            return ""
        logger.error("При несоответствии критериям возвращаем ошибку")
        return "Введены некорректные данные"


def get_mask_account(account_number: Union[int, str]) -> str:
    """функция, которая принимает на вход номер счета и возвращает его маску"""
    logger.info(f"Запрашиваем номер счета для маскировки {account_number}")
    account_number_for_mask = str(account_number)
    if account_number_for_mask.isdigit():
        logger.info("Маскируем номер счета")
        return f"**{account_number_for_mask[-4:]}"
    else:
        if account_number_for_mask == "":
            logger.info("Если номер карты пустой возвращаем пустую строку")
            return ""
        logger.error("При несоответствии критериям возвращаем ошибку")
        return "Введены некорректные данные"


# print("Введите номер карты: ")
# print(get_mask_card_number(card_number=input()))
# print("Введите номер счета: ")
# print(get_mask_account(account_number=input()))
