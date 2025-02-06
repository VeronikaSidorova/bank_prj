import pytest

from src.processing import filter_by_state, sort_by_date

test_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:59.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064591, "state": "CANCELED", "date": "2020-10-12"},
    {"id": 615064591, "state": "CANCELED", "date": ""},
]


@pytest.mark.parametrize(
    "filter_list, state, expected",
    [
        ([], "", []),
        (
            test_list,
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064591, "state": "CANCELED", "date": "2020-10-12"},
                {"id": 615064591, "state": "CANCELED", "date": ""},
            ],
        ),
        (
            test_list,
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:59.425572"},
            ],
        ),
        (test_list, "TIME", []),
    ],
)
def test_filter_by_state(filter_list: list, state: str, expected: list):  # type: ignore
    assert filter_by_state(filter_list, state) == expected


@pytest.mark.parametrize(
    "sort_list, test_sort, expected",
    [
        (
            test_list,
            True,
            [
                {"date": "2020-10-12", "id": 615064591, "state": "CANCELED"},
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-06-30T02:08:59.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "", "id": 615064591, "state": "CANCELED"},
            ],
        ),
        [
            test_list,
            False,
            [
                {"date": "", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "2018-06-30T02:08:59.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "2020-10-12", "id": 615064591, "state": "CANCELED"},
            ],
        ],
    ],
)
def test_sort_by_date(sort_list: list, test_sort: bool, expected: list):  # type: ignore
    assert sort_by_date(sort_list, test_sort) == expected
