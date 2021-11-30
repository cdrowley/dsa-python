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


def test_getIndexElement(setup_unordered_list):
    ul, ul_with_init_items, ul_with_added_items = setup_unordered_list

    for test in [-100, -1 , 0, 1, 100]:
        with pytest.raises(Exception) as e_info:
            ul.getIndexElement(test)
        assert str(e_info.value) == 'Index out of range'
   

    # assuming insertion order (last item added is at index 0))    
    assert ul_with_init_items.getIndexElement(0).getData() == 54
    assert ul_with_init_items.getIndexElement(1).getData() == 26
    assert ul_with_init_items.getIndexElement(2).getData() == 93
    assert ul_with_init_items.getIndexElement(3).getData() == 17
    assert ul_with_init_items.getIndexElement(4).getData() == 77
    assert ul_with_init_items.getIndexElement(5).getData() == 31

    assert ul_with_init_items.getIndexElement(-1).getData() == 31
    assert ul_with_init_items.getIndexElement(-2).getData() == 77
    assert ul_with_init_items.getIndexElement(-3).getData() == 17
    assert ul_with_init_items.getIndexElement(-4).getData() == 93
    assert ul_with_init_items.getIndexElement(-5).getData() == 26
    assert ul_with_init_items.getIndexElement(-6).getData() == 54

    assert ul_with_added_items.getIndexElement(0).getData() == ['x', 'y', 'z']
    assert ul_with_added_items.getIndexElement(1).getData() is None
    assert ul_with_added_items.getIndexElement(2).getData() == 4
    assert ul_with_added_items.getIndexElement(3).getData() == 3
    assert ul_with_added_items.getIndexElement(4).getData() == 'B'
    assert ul_with_added_items.getIndexElement(5).getData() == 'A'

    assert ul_with_added_items.getIndexElement(-1).getData() == 'A'
    assert ul_with_added_items.getIndexElement(-2).getData() == 'B'
    assert ul_with_added_items.getIndexElement(-3).getData() == 3
    assert ul_with_added_items.getIndexElement(-4).getData() == 4
    assert ul_with_added_items.getIndexElement(-5).getData() is None
    assert ul_with_added_items.getIndexElement(-6).getData() == ['x', 'y', 'z']

    for test in [-100, -7, 6, 100]:
        with pytest.raises(Exception) as e_info:
            ul_with_added_items.getIndexElement(test)
        assert str(e_info.value) == 'Index out of range'

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




