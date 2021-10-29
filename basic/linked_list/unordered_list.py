#%%
from __future__ import annotations
from typing import Any
from node import Node


class UnorderedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        elements = []
        current = self.head

        while current is not None:
            elements.append(f"{current.data}-->")
            current = current.next
        return "".join(elements + ["None"])

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
            print(f"{current}--->", end="")
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item: Any) -> None:
        if self.isEmpty():
            raise IndexError("The list is empty.")

        current = self.head
        previous = None

        while current is not None:
            print(f"{current}--->", end="")
            if current.data == item:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print(f"removed")
                return
            previous = current
            current = current.next
        return "test2" if not current and previous else "test3"


# %%
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)

# add tests
# empty raises index error
# 1 item only list
# 5 item list, it takes first, last, every other
# print(mylist.search(12414))
# print(mylist.search(31))
print(mylist)
mylist.remove(26)
print(mylist)
# print(mylist.head.next.data)
# %%
