from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, kw_only=True)
class FunctionView:
    name: str
    result: Any
    arguments: list[str]
    time: str
    memory: str

    def show(self, *, need_result: bool, need_arguments: bool) -> None:
        _result = f' -> {self.result}' if need_result else ''
        _arguments = ', '.join(self.arguments) if need_arguments else ''

        print(f"[time - {self.time}, "
              f"memory - {self.memory}]:  "
              f"{self.name}({_arguments}){_result}")
        