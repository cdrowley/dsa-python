#%%

from __future__ import annotations
from typing import Any

try:
    from basic.linked_list.node import Node
except ModuleNotFoundError:
    from node import Node


class UnorderedList:
    def __init__(self, *items: Any) -> None:
        self.head = None
        self.tail = None
        for item in items:
            self.add(item)

    def __str__(self) -> str:
        nodes = []
        current = self.head

        while current is not None:
            nodes.append(str(current.getData()))
            current = current.getNext()
        return "-->".join(nodes + ["None"])

    def __len__(self) -> int:
        return self.size()

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current
            current = current.getNext()

    def isEmpty(self) -> bool:
        return self.head is None

    def add(self, item: Any) -> None:
        """Adds an items to the head of the list."""
        if not isinstance(item, Node):
            item = Node(item)

        item.setNext(self.head)
        self.head = item
        if self.tail is None:
            self.tail = item

    def size(self) -> int:
        # current = self.head
        # count = 0
        # while current is not None:
        #     count += 1
        #     current = current.getNext()
        # return count
        return len([1 for _ in self])

    def getIndexElement(self, idx: int) -> Node:
        ulsize = self.size()

        if idx < 0:  # allows for negative indexing
            idx = idx + ulsize

        if ulsize == 0 or idx >= ulsize or idx < 0:
            raise IndexError("Index out of range")

        current = self.head
        count = 0
        while current is not None:
            if count == idx:
                return current
            count += 1
            current = current.getNext()

    def search(self, item: Any) -> bool:
        # current = self.head
        # while current is not None:
        #     if current.getData() == item:
        #         return True
        #     current = current.getNext()
        # return False
        for node in self:
            if node.getData() == item:
                return True
        return False

    def remove(self, item: Any) -> None:
        if self.isEmpty():
            raise IndexError("The list is empty.")

        current = self.head
        previous = None

        while current is not None:
            if current.getData() == item:
                if previous is None:  # item is located at the head
                    self.head = current.getNext()
                    if self.head is None:
                        self.tail = None
                else:
                    if current is self.tail:
                        self.tail = previous
                    previous.setNext(current.getNext())
                return
            previous = current
            current = current.getNext()

        if current is None:
            raise ValueError("Item not found.")


if __name__ == "__main__":
    ul = UnorderedList()

    ul_with_init_items = UnorderedList(31)

    ul_with_added_items = UnorderedList()
    for item in ["B", 3, None, ["x", "y", "z"]]:
        ul_with_added_items.add(item)

    for node in ul_with_added_items:
        pass

    ul.add(1)


# %%

# %%
