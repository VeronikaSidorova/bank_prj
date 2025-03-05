import re
from collections import Counter

# from utils import all_transaction


def filter_transactions(transactions: list, search_string: str) -> list:
    # Компилируем регулярное выражение для поиска
    search_pattern = re.compile(search_string, re.IGNORECASE)

    # Фильтруем список словарей по условию
    filtered_transactions = [
        transaction for transaction in transactions if search_pattern.search(transaction.get("description", ""))
    ]

    return filtered_transactions


# print("Введите описание для фильтрации")
# print(filter_transactions(all_transaction("/Users/veronikasidorova/
# bank_prj/data/operations.json"),
# search_string = input()))


def categorize_transactions(transactions: list, categories: str) -> dict:
    # Извлекаем описания из транзакций
    descriptions = [transaction.get("description") for transaction in transactions]

    # Используем Counter для подсчета, отфильтровываем только категории из списка
    category_counts = Counter(desc for desc in descriptions if desc in categories)

    # Приводим к желаемому формату, возвращаем 0, если категории нет
    return {category: category_counts.get(category, 0) for category in categories}


# # print(f"Введите описание для фильтрации")
# search_cat = ["Открытие вклада"]
# print(categorize_transactions(all_transaction("/Users/veronikasidorova/bank_prj/data/operations.json"),
# categories = search_cat))
