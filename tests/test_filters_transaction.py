from src.filters_transaction import categorize_transactions, filter_transactions


def test_filter_transactions(mocker):  # type: ignore
    # Создаем поддельные данные транзакций
    mock_transactions = [
        {"id": 1, "description": "Grocery shopping"},
        {"id": 2, "description": "Online purchase"},
        {"id": 3, "description": "Gas station"},
        {"id": 4, "description": "Gadget store"},
        {"id": 5, "description": "Groceries and more"},
    ]

    # Тест 1: Поиск по слову "Grocery"
    result = filter_transactions(mock_transactions, "Grocery")
    assert len(result) == 1
    assert result[0]["id"] == 1

    # Тест 2: Поиск по слову "online"
    result = filter_transactions(mock_transactions, "online")
    assert len(result) == 1
    assert result[0]["id"] == 2

    # Тест 3: Поиск по слову "store"
    result = filter_transactions(mock_transactions, "store")
    assert len(result) == 1
    assert result[0]["id"] == 4

    # Тест 4: Поиск по слову "nonexistent"
    result = filter_transactions(mock_transactions, "nonexistent")
    assert len(result) == 0

    # Тест 5: Поиск по пустой строке
    result = filter_transactions(mock_transactions, "")
    assert len(result) == 5  # Все транзакции должны быть возвращены


def test_categorize_transactions():  # type: ignore
    # Создаем поддельные данные транзакций
    mock_transactions = [
        {"id": 1, "description": "Grocery shopping"},
        {"id": 2, "description": "Online purchase"},
        {"id": 3, "description": "Gas station"},
        {"id": 4, "description": "Gadget store"},
        {"id": 5, "description": "Groceries and more"},
    ]

    # Определяем категории
    categories = ["Grocery shopping", "Online purchase", "Gas station", "Gadget store"]

    # Вызываем функцию
    result = categorize_transactions(mock_transactions, categories)

    # Проверяем результаты
    assert result["Grocery shopping"] == 1
    assert result["Online purchase"] == 1
    assert result["Gas station"] == 1
    assert result["Gadget store"] == 1
