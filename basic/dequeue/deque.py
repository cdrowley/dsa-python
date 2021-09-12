from typing import Any
from collections.abc import Iterator, Iterable


class Deque:
    def __init__(self, *items: Any) -> None:
        self.items = [i for i in items]

    def __str__(self) -> str:
        return f"{self.items}"

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.items)

    def __getitem__(self, item) -> Iterable[Any]:
        return self.items[item]

    def __reversed__(self):
        for item in self.items[::-1]:
            yield item

    def reverse(self) -> None:
        self.items = self.items[::-1]

    def isEmpty(self) -> bool:
        return True if not self.items else False

    def size(self) -> int:
        return len(self)

    def addFront(self, item) -> None:
        self.items.append(item)

    def addRear(self, item) -> None:
        self.items.insert(0, item)

    def removeFront(self) -> Any:
        return self.items.pop()

    def removeRear(self) -> Any:
        return self.items.pop(0)
