import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def number_1() -> str:
    return "Счет 12345678901234567890"


def test_mask_account_or_card(number_1: str):  # type: ignore
    assert mask_account_card(number_1) == "Счет **7890"


@pytest.mark.parametrize(
    "number_2, expected",
    [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"), ("карта", "Введены некорректные данные"), ("", "")],
)
def test_mask_account(number_2: str, expected: str):  # type: ignore
    assert mask_account_card(number_2) == expected


@pytest.fixture
def date_1() -> str:
    return "2024-03-11T02:26:18.671407"


def test_date(date_1: str):  # type: ignore
    assert get_date(date_1) == "11.03.2024"


@pytest.mark.parametrize("date_2, expected", [("2025-01-01", "01.01.2025"), ("2025 01 01", "01.01.2025"), ("", "")])
def test_get_date(date_2: str, expected: str):  # type: ignore
    assert get_date(date_2) == expected
