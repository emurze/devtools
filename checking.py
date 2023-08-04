import functools
import tracemalloc
from collections.abc import Callable
from time import perf_counter
from typing import Any, Optional

from devtools.modules.transform import Transform
from devtools.modules.views import FunctionView


def checking(_func: Optional[Callable] = None, *,
             arguments: bool = False, result: bool = False):
    """This decorator count function time and memory"""
    def check(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            _args = (str(x) for x in args)
            _kwargs = (f'{k}={v}' for k, v in kwargs.items())
            _arguments: list[str] = [*_args, *_kwargs]

            tracemalloc.start()
            t0 = perf_counter()

            _result = func(*args, **kwargs)

            time = Transform.get_time(perf_counter() - t0)
            memory = Transform.get_memory(tracemalloc.get_traced_memory()[-1])

            view = FunctionView(
                name=func.__name__,
                result=_result,
                arguments=_arguments,
                time=time,
                memory=memory,
            )
            view.show(need_result=result, need_arguments=arguments)

            tracemalloc.stop()
            return _result
        return wrapper
    return check(_func) if _func else check
