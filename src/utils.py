import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def all_transaction(json_file) -> list:  # type: ignore
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция
    возвращает пустой список."""
    try:
        logger.info("Функция получает путь до файла json")
        with open(json_file, "r") as f:
            logger.info("Распаковываем файл json")
            transaction = json.load(f)
            if isinstance(transaction, list):
                logger.info("Если из файла получен список, то функция его возвращает")
                return transaction
            return []
    except FileNotFoundError:
        logger.error("Произошла ошибка: файл не найден, возвращается пустой список")
        return []
    except json.JSONDecodeError:
        logger.error("Произошла ошибка: некорректный файл, возвращается пустой список")
        return []


# if __name__ == '__main__':
#     print(all_transaction('../data/operations.json'))
