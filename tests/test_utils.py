from unittest.mock import mock_open, patch

from src.utils import all_transaction


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_all_transaction(mock_file):  # type: ignore
    result = all_transaction(mock_file)
    assert result == []
    mock_file.assert_called_once_with(mock_file, "r")


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
def test_valid_json_file(mock_file):  # type: ignore
    result = all_transaction(mock_file)
    assert result == [{"id": 1, "amount": 100}]


@patch("builtins.open", new_callable=mock_open, read_data="not a json")
def test_invalid_json_file(mock_file):  # type: ignore
    result = all_transaction(mock_file)
    assert result == []


def test_file_not_found():  # type: ignore
    result = all_transaction("non_existent_file.json")
    assert result == []
