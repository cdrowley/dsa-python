from basic.linked_list.unordered_list import UnorderedList
import pytest


@pytest.fixture
def setup_unordered_list():
    ul = UnorderedList()
    ul_with_init_items = UnorderedList(31, 77, 17, 93, 26, 54)

    ul_with_added_items = UnorderedList()
    for item in ["B", 3, None, ["x", "y", "z"]]:
        ul_with_added_items.add(item)

    return ul, ul_with_init_items, ul_with_added_items


def test_isEmpty_size(setup_unordered_list):
    ul, ul_with_init_items, ul_with_added_items = setup_unordered_list

    assert ul.isEmpty() == True
    assert ul_with_init_items.isEmpty() == False
    assert ul_with_added_items.isEmpty() == False

    assert ul.size() == 0
    assert ul_with_init_items.size() == 6
    assert ul_with_added_items.size() == 4


def test_dunder_methods(setup_unordered_list):
    ul, ul_with_init_items, ul_with_added_items = setup_unordered_list

    assert str(ul) == "None"
    assert str(ul_with_init_items) == "54-->26-->93-->17-->77-->31-->None"
    assert str(ul_with_added_items) == "['x', 'y', 'z']-->None-->3-->B-->None"

    assert len(ul) == 0
    assert len(ul_with_init_items) == 6
    assert len(ul_with_added_items) == 4

    assert [node.getData() for node in ul] == []
    assert [node.getData() for node in ul_with_init_items] == [54, 26, 93, 17, 77, 31]
    assert [node.getData() for node in ul_with_added_items] == [
        ["x", "y", "z"],
        None,
        3,
        "B",
    ]


def test_getIndexElement(setup_unordered_list):
    ul, ul_with_init_items, ul_with_added_items = setup_unordered_list

    for test in [-100, -1, 0, 1, 100]:
        with pytest.raises(IndexError) as e_info:
            ul.getIndexElement(test)
        assert str(e_info.value) == "Index out of range"

    for test in [-100, -7, 6, 100]:
        with pytest.raises(IndexError) as e_info:
            ul_with_added_items.getIndexElement(test)
        assert str(e_info.value) == "Index out of range"

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

    assert ul_with_added_items.getIndexElement(0).getData() == ["x", "y", "z"]
    assert ul_with_added_items.getIndexElement(1).getData() is None
    assert ul_with_added_items.getIndexElement(2).getData() == 3
    assert ul_with_added_items.getIndexElement(3).getData() == "B"

    assert ul_with_added_items.getIndexElement(-1).getData() == "B"
    assert ul_with_added_items.getIndexElement(-2).getData() == 3
    assert ul_with_added_items.getIndexElement(-3).getData() is None
    assert ul_with_added_items.getIndexElement(-4).getData() == ["x", "y", "z"]


def test_search(setup_unordered_list):
    ul, ul_with_init_items, ul_with_added_items = setup_unordered_list

    assert ul.search("Not in list") == False
    assert ul.search(None) == False

    assert ul_with_init_items.search(54) == True
    assert ul_with_init_items.search(26) == True
    assert ul_with_init_items.search(93) == True
    assert ul_with_init_items.search(17) == True
    assert ul_with_init_items.search(77) == True
    assert ul_with_init_items.search(31) == True
    assert ul_with_init_items.search("Not in list") == False

    assert ul_with_added_items.search(["x", "y", "z"]) == True
    assert ul_with_added_items.search(None) == True
    assert ul_with_added_items.search(3) == True
    assert ul_with_added_items.search("B") == True
    assert ul_with_added_items.search("Not in list") == False


def test_remove(setup_unordered_list):
    ul, ul_with_init_items, ul_with_added_items = setup_unordered_list

    additional_item = "ABCDEFG"
    # test empty list
    with pytest.raises(IndexError) as e_info:
        ul.remove(additional_item)
        assert str(e_info.value) == "The list is empty."

    # test adding and removing
    ul.add(additional_item)
    assert len(ul) == 1
    ul.remove(additional_item)
    assert len(ul) == 0

    # test removing all elements
    for item in [31, 77, 17, 93, 26, 54][::-1]:
        ul_with_init_items.remove(item)
    assert len(ul_with_init_items) == 0

    # ["B", 3, None, ["x", "y", "z"]]
    assert ul_with_added_items.tail.getData() == "B"
    assert ul_with_added_items.head.getData() == ["x", "y", "z"]
    assert ul_with_added_items.head.getNext().getData() is None

    # test removing from the middle
    ul_with_added_items.remove(3)
    assert len(ul_with_added_items) == 3

    # test removing from the end
    ul_with_added_items.remove("B")
    assert len(ul_with_added_items) == 2

    assert ul_with_added_items.tail.getData() is None
    assert ul_with_added_items.head.getData() == ["x", "y", "z"]

    # test removing from the beginning
    ul_with_added_items.add(additional_item)
    assert ul_with_added_items.head.getData() == additional_item
    assert ul_with_added_items.tail.getData() is None

    ul_with_added_items.remove(None)
    assert ul_with_added_items.tail.getData() == ["x", "y", "z"]

    ul_with_added_items.remove(["x", "y", "z"])
    assert ul_with_added_items.tail.getData() == additional_item
    assert ul_with_added_items.head.getData() == additional_item

    ul_with_added_items.remove(additional_item)
    assert len(ul_with_added_items) == 0
    assert ul_with_added_items.tail is None
    assert ul_with_added_items.head is None
