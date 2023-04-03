import functools
import tracemalloc
from collections.abc import Callable
from time import perf_counter
from typing import Any, Union

from .modules.views import View


def checking(_func: Union[Callable, None] = None, *, result: bool = False):
    """This decorator count func time and memory"""
    def check(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            tracemalloc.start()
            t0 = perf_counter()
            res = func(*args, **kwargs)
            args_list = [str(x) for x in args]
            args_list.extend(f'{k}={v}' for k, v in kwargs.items())
            View.show(args_list, name=func.__name__, time=perf_counter()-t0,
                      amount=tracemalloc.get_traced_memory()[-1],
                      func_res=res, result=result)
            tracemalloc.stop()
            return res
        return wrapper
    return check if _func is None else check(_func)
