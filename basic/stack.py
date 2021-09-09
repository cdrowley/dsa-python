from typing import Any


class Stack:
    def __init__(self, *args) -> None:
        self.items = []
        if args:
            for arg in args:
                self.items.append(arg)

    def __len__(self):
        return len(self.items)

    def __str__(self) -> str:
        return f"{self.items}"

    def __iter__(self):
        return iter(self.items)

    def isEmpty(self) -> bool:
        return False if self.items else True

    def size(self) -> int:
        return len(self)

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        return self.items.pop()

    def peek(self) -> Any:
        return self.items[-1]
