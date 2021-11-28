from basic.linked_list.unordered_list import UnorderedList
import pytest


@pytest.fixture
def setup_unordered_list():
    ul = UnorderedList()

    ul_with_init_items = UnorderedList(31, 77, 17, 93, 26, 54)

    ul_with_added_items = UnorderedList()
    for item in ['A', 'B', 3, 4, None, ['x', 'y', 'z']]:
        ul_with_added_items.add(item)

    return ul, ul_with_init_items, ul_with_added_items




# print(mylist.size())
# print(mylist.search(93))
# print(mylist.search(100))

# mylist.add(100)
# print(mylist.search(100))
# print(mylist.size())

# mylist.remove(54)
# print(mylist.size())
# mylist.remove(93)
# print(mylist.size())
# mylist.remove(31)
# print(mylist.size())
# print(mylist.search(93))




