import pytest

from src.widget import mask_account_card, get_date

@pytest.fixture
def number_1():
    return 'Счет 12345678901234567890'

def test_mask_account_or_card(number_1):
    assert mask_account_card(number_1) == "Счет **7890"


@pytest.mark.parametrize("number_2, expected", [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('карта', 'Введены некорректные данные'),
    ('', '')])
def test_mask_account(number_2, expected):
    assert mask_account_card(number_2) == expected


@pytest.fixture
def date_1():
    return "2024-03-11T02:26:18.671407"

def test_date(date_1):
    assert get_date(date_1) == "11.03.2024"

@pytest.mark.parametrize("date_2, expected", [
    ('2025-01-01', '01.01.2025'),
    ('2025 01 01', '01.01.2025'),
    ('', '')])
def test_get_date(date_2, expected):
    assert get_date(date_2) == expected
