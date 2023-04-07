from dataclasses import dataclass, field
from typing import NoReturn

from ...modules.view.transform import Transform  # type: ignore
from ...modules.exceptions import SetupDoesNotActivated  # type: ignore


@dataclass(kw_only=True)
class View:
    """View for checking"""
    args: list[str] | str = field(kw_only=False)
    name: str
    time: float
    amount: int
    func_res: str
    is_changed: bool = field(default=False, repr=False)

    def show(self) -> None | NoReturn:
        """Transform and print data"""
        if not self.is_changed:
            raise SetupDoesNotActivated
        print(f"[time - {Transform.get_time(self.time)}, "
              f"memory - {Transform.get_memory(self.amount)}]:  "
              f"{self.name}({self.args}){self.func_res}")
        return None  # for mypy

    def setup(self, *, chk_result: bool, chk_arguments: bool) -> None:
        if not self.is_changed:
            self.is_changed = True
        self.func_res = f' -> {self.func_res}' if chk_result else ''
        self.args = ', '.join(self.args) if chk_arguments else ''
