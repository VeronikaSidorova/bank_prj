from unittest.mock import patch

import pandas as pd

from src.reader_csv_and_excel import reader_csv, reader_excel


# Мокируем pd.read_csv
@patch("pandas.read_csv")
def test_reader_csv(mock_read_csv):  # type: ignore
    # Настраиваем мок, чтобы он возвращал DataFrame
    mock_read_csv.return_value = pd.DataFrame({"column1": [1, 2, 3], "column2": ["a", "b", "c"]})

    expected = [{"column1": 1, "column2": "a"}, {"column1": 2, "column2": "b"}, {"column1": 3, "column2": "c"}]

    result = reader_csv("test.csv")
    assert result == expected


# Мокируем pd.read_excel
@patch("pandas.read_excel")
def test_reader_excel(mock_read_excel):  # type: ignore
    # Настраиваем мок, чтобы он возвращал DataFrame
    mock_read_excel.return_value = pd.DataFrame({"column1": [1, 2, 3], "column2": ["a", "b", "c"]})

    expected = [{"column1": 1, "column2": "a"}, {"column1": 2, "column2": "b"}, {"column1": 3, "column2": "c"}]

    result = reader_excel("test.xlsx")
    assert result == expected
