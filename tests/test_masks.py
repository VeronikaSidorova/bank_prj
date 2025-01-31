import pytest

from src.masks import get_mask_card_number

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




