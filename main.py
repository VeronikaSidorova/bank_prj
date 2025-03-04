from src.filters_transaction import filter_transactions
from src.processing import filter_by_state, sort_by_date
from src.reader_csv_and_excel import reader_csv, reader_excel
from src.utils import all_transaction
from src.widget import get_date, mask_account_card


def main():  # type: ignore
    finish_list = []
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями. "
        "\nВыберите необходимый пункт меню:"
        "\n1. Получить информацию о транзакциях из JSON-файла"
        "\n2. Получить информацию о транзакциях из CSV-файла"
        "\n3. Получить информацию о транзакциях из XLSX-файла"
    )
    file_choice = input("Пользователь: ")

    if file_choice == "1":
        finish_list = all_transaction("/Users/veronikasidorova/bank_prj/data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif file_choice == "2":
        finish_list = reader_csv("/Users/veronikasidorova/bank_prj/data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif file_choice == "3":
        finish_list = reader_excel("/Users/veronikasidorova/bank_prj/data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        main()

    def found_status(filter_list):  # type: ignore
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        statuses = {"EXECUTED", "CANCELED", "PENDING"}
        status_choice = input("Пользователь: ").upper()

        if status_choice in statuses:
            print(f'Операции отфильтрованы по статусу "{status_choice}"')
            return filter_by_state(filter_list, status_choice)
        else:
            print(f'Статус операции "{status_choice}" недоступен.')
            found_status(filter_list)

    finish_list_1 = found_status(finish_list)
    #
    # finish_list_2 = []
    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        result = input("Отсортировать по возрастанию или по убыванию? \nПользователь: ").lower()
        if result == "по возрастанию":
            finish_list_2 = sort_by_date(finish_list_1, False)
        else:
            finish_list_2 = sort_by_date(finish_list_1)
    else:
        finish_list_2 = finish_list_1

    finish_list_3 = []
    currency_filter = input("Выводить только рублевые транзакции? Да/Нет" "\nПользователь: ").strip().lower()
    if currency_filter == "да":
        for transaction in finish_list_2:
            if "RUB" in str(transaction["operationAmount"]["currency"]["code"]):
                finish_list_3.append(transaction)
    else:
        finish_list_3 = finish_list_2

    finish_list_4 = []
    keyword_filter = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет" "\nПользователь: ")
        .strip()
        .lower()
    )
    if keyword_filter == "да":
        keyword = input("Введите слово для фильтрации по описанию: ")
        finish_list_4 = filter_transactions(finish_list_3, keyword)
    else:
        finish_list_4 = finish_list_3

    print("Распечатываю итоговый список транзакций...")

    if finish_list_4:
        print(f"Всего банковских операций в выборке: {len(finish_list_4)}")
        for transaction in finish_list_4:
            print(f"{get_date(transaction["date"])} {transaction["description"]}")
            if transaction.get("from", ""):
                print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
            else:
                print(f"{mask_account_card(transaction["to"])}")
            if transaction.get("amount", ""):
                print(f"Сумма: {transaction["amount"]} {transaction["currency_code"]}")
            else:
                print(
                    f"Сумма: {transaction["operationAmount"]["amount"]} "
                    f"{transaction["operationAmount"]["currency"]["name"]}"
                )
            print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    print(main())
