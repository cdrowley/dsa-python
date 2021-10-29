from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, initdata) -> None:
        self.data = initdata
        self.next = None

    def __str__(self) -> str:
        return f"{self.data}"

    def getData(self) -> Any:
        return self.data

    def getNext(self) -> Node:
        return self.next

    def setData(self, newdata: Any) -> None:
        self.data = newdata

    def setNext(self, newnext: Node) -> None:
        self.next = newnext
