import pytest

from src.decorators import log, my_function


def test_my_function_success(capsys): # type: ignore
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_my_function_error(capsys):  # type: ignore
    @log()
    def faulty_function(x, y):  # type: ignore
        return x / y

    with pytest.raises(ZeroDivisionError):
        faulty_function(1, 0)

    captured = capsys.readouterr()
    assert "faulty_function error: ZeroDivisionError" in captured.err


def test_log_to_file():  # type: ignore
    log_file = "test_log.txt"

    @log(filename=log_file)
    def add(a, b):  # type: ignore
        return a + b

    add(3, 4)

    with open(log_file, "r") as f:
        logs = f.readlines()

    assert any("add ok" in log for log in logs)
