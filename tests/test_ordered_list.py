from basic.linked_list.ordered_list import OrderedList
import pytest


@pytest.fixture
def setup_ordered_list():
    ol = OrderedList()
    ol_with_init_items = OrderedList(31, 26, 17, 54, 93, 77)

    ol_with_added_items = OrderedList()
    for item in [2, 0, 3, 1]:
        ol_with_added_items.add(item)

    return ol, ol_with_init_items, ol_with_added_items


def test_isEmpty_size(setup_ordered_list):
    ol, ol_with_init_items, ol_with_added_items = setup_ordered_list

    assert ol.isEmpty() == True
    assert ol_with_init_items.isEmpty() == False
    assert ol_with_added_items.isEmpty() == False

    assert ol.size() == 0
    assert ol_with_init_items.size() == 6
    assert ol_with_added_items.size() == 4


def test_dunder_methods(setup_ordered_list):
    ol, ol_with_init_items, ol_with_added_items = setup_ordered_list

    assert str(ol) == "None"
    assert str(ol_with_init_items) == "17-->26-->31-->54-->77-->93-->None"
    assert str(ol_with_added_items) == "0-->1-->2-->3-->None"

    assert len(ol) == 0
    assert len(ol_with_init_items) == 6
    assert len(ol_with_added_items) == 4

    assert [node.getData() for node in ol] == []
    assert [node.getData() for node in ol_with_init_items] == [17, 26, 31, 54, 77, 93]
    assert [node.getData() for node in ol_with_added_items] == [0, 1, 2, 3]


def test_getIndexElement(setup_ordered_list):
    ol, ol_with_init_items, ol_with_added_items = setup_ordered_list

    for test in [-100, -1, 0, 1, 100]:
        with pytest.raises(IndexError) as e_info:
            ol.getIndexElement(test)
        assert str(e_info.value) == "Index out of range"

    for test in [-100, -7, 6, 100]:
        with pytest.raises(IndexError) as e_info:
            ol_with_added_items.getIndexElement(test)
        assert str(e_info.value) == "Index out of range"

    # assuming insertion order (smallest number added is at index 0))
    assert ol_with_init_items.getIndexElement(0).getData() == 17
    assert ol_with_init_items.getIndexElement(1).getData() == 26
    assert ol_with_init_items.getIndexElement(2).getData() == 31
    assert ol_with_init_items.getIndexElement(3).getData() == 54
    assert ol_with_init_items.getIndexElement(4).getData() == 77
    assert ol_with_init_items.getIndexElement(5).getData() == 93

    assert ol_with_init_items.getIndexElement(-1).getData() == 93
    assert ol_with_init_items.getIndexElement(-2).getData() == 77
    assert ol_with_init_items.getIndexElement(-3).getData() == 54
    assert ol_with_init_items.getIndexElement(-4).getData() == 31
    assert ol_with_init_items.getIndexElement(-5).getData() == 26
    assert ol_with_init_items.getIndexElement(-6).getData() == 17

    assert ol_with_added_items.getIndexElement(0).getData() == 0
    assert ol_with_added_items.getIndexElement(1).getData() == 1
    assert ol_with_added_items.getIndexElement(2).getData() == 2
    assert ol_with_added_items.getIndexElement(3).getData() == 3

    assert ol_with_added_items.getIndexElement(-1).getData() == 3
    assert ol_with_added_items.getIndexElement(-2).getData() == 2
    assert ol_with_added_items.getIndexElement(-3).getData() == 1
    assert ol_with_added_items.getIndexElement(-4).getData() == 0


def test_search(setup_ordered_list):
    ol, ol_with_init_items, ol_with_added_items = setup_ordered_list

    for test in ["Not in list", 1, None]:
        assert ol.search(test) == False

    for test in [17, 26, 31, 54, 77, 93]:
        assert ol_with_init_items.search(test) == True

    for test in [0, 1, 2, 3]:
        assert ol_with_added_items.search(test) == True


def test_remove(setup_ordered_list):
    ol, ol_with_init_items, ol_with_added_items = setup_ordered_list

    additional_item = 999
    # test empty list
    with pytest.raises(IndexError) as e_info:
        ol.remove(additional_item)
        assert str(e_info.value) == "The list is empty."

    # test adding and removing
    ol.add(additional_item)
    assert len(ol) == 1
    ol.remove(additional_item)
    assert len(ol) == 0

    # test removing all elements
    for item in [31, 77, 17, 93, 26, 54]:
        ol_with_init_items.remove(item)
    assert len(ol_with_init_items) == 0

    # [0, 1, 2, 3]
    assert ol_with_added_items.tail.getData() == 3
    assert ol_with_added_items.head.getData() == 0
    assert ol_with_added_items.head.getNext().getData() == 1

    # # test removing from the middle
    ol_with_added_items.remove(1)
    assert len(ol_with_added_items) == 3

    # # test removing from the end
    ol_with_added_items.remove(3)
    assert len(ol_with_added_items) == 2

    assert ol_with_added_items.tail.getData() == 2
    assert ol_with_added_items.head.getData() == 0

    # # test removing from the beginning
    ol_with_added_items.add(additional_item)
    assert ol_with_added_items.head.getData() == 0
    assert ol_with_added_items.tail.getData() == 999

    ol_with_added_items.remove(999)
    assert ol_with_added_items.tail.getData() == 2
