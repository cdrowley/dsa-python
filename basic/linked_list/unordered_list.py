from __future__ import annotations
from typing import Any
from node import Node


class UnorderedList:
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self) -> bool:
        return self.head is None

    def add(self, item: Any) -> None:
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self) -> int:
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next
        return count

    def getIndexElement(self, idx: int) -> Node:
        current = self.head
        count = 0
        while current is not None:
            if count == idx:
                return current
            count += 1
            current = current.next
        else:
            raise IndexError("The list is not that long.")

    def search(self, item: Any) -> bool:
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item: Any) -> None:
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                if previous is None:
                    self.head = current
                else:
                    previous.next = current
                return
            previous = current
            current = current.next
        return current.data


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

# print(mylist.search(12414))
print(mylist.remove(12414124))
