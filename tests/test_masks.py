import pytest

from src.masks import get_mask_card_number

@pytest.fixture
def my_card_number():
    return 1234123412341234


def test_mask_card_number(my_card_number):
    assert get_mask_card_number(my_card_number) == "1234 12** **** 1234"
