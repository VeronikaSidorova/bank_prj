import functools
import logging
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    # Настройка логирования
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
    logger.addHandler(handler)

    def decorator(func: Any) -> Any:
        @functools.wraps(func)
        def wrapper(*args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Any:
            try:
                # Логируем начало выполнения функции
                logger.info(f"Starting execution of {func.__name__}")
                result = func(*args, **kwargs)
                # Логируем успешное завершение
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                # Логируем ошибку
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator


@log()
def my_function(x: int, y: int) -> int:
    return x + y


print(my_function(1, 2))
