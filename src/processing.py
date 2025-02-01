def filter_by_state(list_for_filter: list[dict[str, str | int]], state: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и опционально
    значение для ключа state(по умолчанию 'EXECUTED'). Функция
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    filter_list_by_state = []
    for find_state in list_for_filter:
        if find_state["state"] == state:
            filter_list_by_state.append(find_state)
        else:
            continue
    return filter_list_by_state


def sort_by_date(list_date_for_filter: list[dict[str, str | int]], sort_order: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный
    параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате"""
    return sorted(list_date_for_filter, key=lambda x: x["date"], reverse=sort_order)


filter_list: list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:59.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064591, "state": "CANCELED", "date": "2020-10-12"},
    {"id": 615064591, "state": "CANCELED", "date": ""},
]
print(filter_by_state(filter_list))
print(sort_by_date(filter_list))
