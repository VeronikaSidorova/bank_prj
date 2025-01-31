import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number_1():
    return 1234123412341234

def test_mask_card_number(card_number_1):
    assert get_mask_card_number(card_number_1) == "1234 12** **** 1234"


@pytest.mark.parametrize("card_number_2, expected", [
    (12341234123412345, 'Введены некорректные данные'),
    (1234, 'Введены некорректные данные'),
    ('карта', 'Введены некорректные данные'),
    ('', ''),
    ('1234123412341234', '1234 12** **** 1234')])
def test_card(card_number_2, expected):
    assert get_mask_card_number(card_number_2) == expected


@pytest.fixture
def account_number_1():
    return 12345678901234567890

def test_mask_account(account_number_1):
    assert get_mask_account(account_number_1) == "**7890"


@pytest.mark.parametrize("account_number_2, expected", [
    (112345678901234, '**1234'),
    ('1234567890', '**7890'),
    ('счет', 'Введены некорректные данные'),
    ('', '')])
def test_account(account_number_2, expected):
    assert get_mask_account(account_number_2) == expected