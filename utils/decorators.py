import logging
import logging.config
import time
from functools import wraps
from typing import Callable

import pandas as pd

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_time(func: Callable) -> Callable:
    @wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        time_taken = time.time() - start
        logging.info(f"{time_taken=} by function {func.__name__}")
        return result

    return _wrapper


def log_info(func: Callable) -> Callable:
    @wraps(func)
    def _wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} executed successfully. {result=}")
        return result

    return _wrapper


def assert_shape(group_by: list | str):
    def _upper_wrap(func: Callable | pd.DataFrame):
        if isinstance(group_by, str):
            grouper = [x.strip() for x in group_by.split(",")]
        elif isinstance(group_by, list):
            grouper = group_by
        else:
            raise ValueError(
                f"Invalid type, only str and list supported, got {type(group_by)}"
            )

        if isinstance(func, Callable):

            @wraps(func)
            def _wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                assert result.shape[0] == result.groupby(grouper).ngroups
                return result

            return _wrapper

        elif isinstance(func, pd.DataFrame):
            assert func.shape[0] == func.groupby(grouper).ngroups
            return func

    return _upper_wrap
