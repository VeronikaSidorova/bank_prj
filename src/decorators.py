import functools
import logging
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Настройка логирования"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    if filename is None:
        handler = logging.StreamHandler()
    else:
        handler = logging.FileHandler(filename)
    logger.addHandler(handler)

    def decorator(func: Any) -> Any:
        """Декоратор, который проверит правильность выполнения функции"""

        @functools.wraps(func)
        def wrapper(*args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Any:
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                print(f"{func.__name__} ok")
                return result
            except Exception as e:
                # Логируем ошибку
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise  # logger.error

        return wrapper

    return decorator


@log()
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
