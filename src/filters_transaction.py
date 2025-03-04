import re

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
    # Создаем словарь для хранения категорий и их счетчиков
    category_counts = {category: 0 for category in categories}

    # Проходим по списку транзакций
    for transaction in transactions:
        descript = transaction.get("description", "")

        # Увеличиваем счетчик в соответствующей категории, если найдено совпадение
        for category in categories:
            if category in descript:
                category_counts[category] += 1

    return category_counts


# print(f"Введите описание для фильтрации")
# search_cat = ["Перевод"]
# print(categorize_transactions(all_transaction("/Users/veronikasidorova/
# bank_prj/data/operations.json"),
# categories = search_cat))
