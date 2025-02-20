from unittest.mock import MagicMock, patch

from src.external_api import convertion_func


@patch("requests.request")
def test_conversion_from_rub(mock_request):  # type: ignore
    transaction_list = [{"operationAmount": {"currency": {"code": "RUB"}, "amount": "100.0"}}]
    result = list(convertion_func(transaction_list))
    assert result == [100.0]


@patch("requests.request")
def test_conversion_from_usd(mock_request):  # type: ignore
    transaction_list = [{"operationAmount": {"currency": {"code": "USD"}, "amount": "100.0"}}]
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.0}
    mock_request.return_value = mock_response
    result = list(convertion_func(transaction_list))
    assert result == [7500.0]


@patch("requests.request")
def test_conversion_from_eur(mock_request):  # type: ignore
    transaction_list = [{"operationAmount": {"currency": {"code": "EUR"}, "amount": "100.0"}}]
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 8500.0}
    mock_request.return_value = mock_response
    result = list(convertion_func(transaction_list))
    assert result == [8500.0]
