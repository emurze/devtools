class View:
    """View for checking"""

    @staticmethod
    def show(args, *, name: str, time: float, amount: int,
             func_res: str, result: bool) -> None:
        """To view and to show"""
        func_view = f' -> {func_res}' if result else ''
        args_view = ", ".join(args)
        print(f"[time - {View.get_time(time)}, "
              f"memory - {View.get_memory(amount)}]:  "
              f"{name}({args_view}){func_view}")

    @staticmethod
    def get_memory(amount: int, /) -> str:
        """Transform bits to bytes and bytes to KB, MB, GB"""
        amount //= 8
        ext = 'B'
        extensions = ["KB", "MB", "GB", "TB"]
        while amount > 1000 and len(extensions) > 0:
            ext = extensions.pop(0)
            amount //= 1000
        return f"{amount:.0f} {ext}"

    @staticmethod
    def get_time(time: float, /) -> str:
        """Transform time format in s and ms"""
        ext = 's'
        if time < 0.001:
            ext = 'ms'
            time *= 1000
        return f"{time:.3f}{ext}"
