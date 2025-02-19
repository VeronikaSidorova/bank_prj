from unittest.mock import Mock, patch, mock_open

from src.utils import all_transaction


@patch('builtins.open', new_callable=mock_open, read_data='')
def test_all_transaction(mock_file):
    result = all_transaction(mock_file)
    assert result == []
    mock_file.assert_called_once_with(mock_file, 'r')