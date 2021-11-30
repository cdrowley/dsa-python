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
        for item in items:
            self.add(item)

    def __str__(self) -> str:
        elements = []
        current = self.head

        while current is not None:
            elements.append(f"{current.data}-->")
            current = current.getNext()
        return "".join(elements + ["None"])

    def __len__(self) -> int:
        return self.size()

    def __iter__(self) -> Iterator[Any]:
        items = []
        current = self.head
        count = 0
        while current is not None:
            count += 1
            items.append(current.getData())
            current = current.getNext()
        return iter(items)

    def isEmpty(self) -> bool:
        return self.head is None

    def add(self, item: Any) -> None:
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self) -> int:
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def getIndexElement(self, idx: int) -> Node:
        ulsize = self.size()
        
        if idx < 0: # allows for negative indexing
            idx =  idx + ulsize

        if ulsize == 0 or idx >= ulsize or idx < 0:
            raise IndexError('Index out of range')

        current = self.head
        count = 0
        while current is not None:
            if count == idx:
                return current
            count += 1
            current = current.getNext()

    def search(self, item: Any) -> bool:
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self, item: Any) -> None:
        if self.isEmpty():
            raise IndexError("The list is empty.")

        current = self.head
        previous = None

        while current is not None:
            if current.getData() == item:
                if previous is None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext()) 
                return
            previous = current
            current = current.getNext()
        
        if current is None:
            raise ValueError("Item not found.")


#x = UnorderedList()

#print(x.size())

#if __name__ == '__main__':
#    pass
# %%
