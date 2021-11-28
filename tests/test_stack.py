import pytest
from basic.stack.stack import Stack


@pytest.fixture
def setup_stacks():
    s = Stack()
    s_with_items = Stack(1, 2, 3, True, None, "ABC")
    return s, s_with_items


def test_stack_init(setup_stacks):
    s, s_with_items = setup_stacks
    assert list(s) == []
    assert list(s_with_items) == [1, 2, 3, True, None, "ABC"]


def test_isEmpty(setup_stacks):
    s, s_with_items = setup_stacks
    assert s.isEmpty() == True
    assert s_with_items.isEmpty() == False


def test_size_len(setup_stacks):
    s, s_with_items = setup_stacks
    assert s.size() == 0
    assert s_with_items.size() == 6
    assert len(s_with_items) == 6


def test_push_peek_pop(setup_stacks):
    s, s_with_items = setup_stacks
    s.push(4)
    assert s.isEmpty() == False
    assert s.peek() == 4
    assert s.pop() == 4 and len(s) == 0

    with pytest.raises(IndexError):
        s.pop()

    s_with_items.push("dog")
    assert s_with_items.isEmpty() == False
    assert s_with_items.peek() == "dog"

    for _ in range(len(s_with_items)):
        s_with_items.pop()

    assert len(s_with_items) == 0

    with pytest.raises(IndexError):
        s_with_items.pop()


def test_str(setup_stacks):
    s, s_with_items = setup_stacks
    assert str(s) == "[]"
    assert str(s_with_items) == "[1, 2, 3, True, None, 'ABC']"


def test_iter(setup_stacks):
    s, s_with_items = setup_stacks
    s.push(4)
    assert all(True for i in s if i == 4)
    assert all(True for i in s_with_items if i in (1, 2, 3, True, None, "ABC"))