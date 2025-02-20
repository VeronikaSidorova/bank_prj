import json


def all_transaction(json_file) -> list:  # type: ignore
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция
    возвращает пустой список."""
    try:
        with open(json_file, "r") as f:
            transaction = json.load(f)
            if isinstance(transaction, list):
                return transaction
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# if __name__ == '__main__':
#     print(all_transaction('../data/operations.json'))
