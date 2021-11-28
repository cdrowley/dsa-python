import pytest
from basic.dequeue.deque import Deque


@pytest.fixture
def setup_deque():
    d = Deque()
    d_with_items = Deque(1, 2, 3, True, None, "ABC")
    return d, d_with_items


def test_deque_init(setup_deque):
    d, d_with_items = setup_deque
    assert list(d) == []
    assert list(d_with_items) == [1, 2, 3, True, None, "ABC"]


def test_isEmpty(setup_deque):
    d, d_with_items = setup_deque
    assert d.isEmpty() == True
    assert d_with_items.isEmpty() == False


def test_size_len(setup_deque):
    d, d_with_items = setup_deque
    assert d.size() == 0
    assert d_with_items.size() == 6
    assert len(d_with_items) == 6


def test_add_remove_front():
    q = Deque()
    assert q.isEmpty() == True

    q.addFront(4)
    q.addFront("dog")
    q.addFront(True)
    assert q.size() == 3
    assert q.isEmpty() == False

    assert q.removeFront() == True
    assert q.removeRear() == 4
    assert q.removeFront() == "dog"

    assert q.size() == 0


def test_add_remove_rear():
    q = Deque()
    assert q.isEmpty() == True

    q.addRear(4)
    q.addRear("dog")
    q.addRear(True)
    assert q.size() == 3
    assert q.isEmpty() == False

    assert q.removeRear() == True
    assert q.removeFront() == 4
    assert q.removeRear() == "dog"

    assert q.size() == 0


def test_str(setup_deque):
    d, d_with_items = setup_deque
    assert str(d) == "[]"
    assert str(d_with_items) == "[1, 2, 3, True, None, 'ABC']"


def test_iter(setup_deque):
    d, d_with_items = setup_deque
    d.addFront(4)
    assert all(True for i in d if i == 4)
    assert all(True for i in d_with_items if i in (1, 2, 3, True, None, "ABC"))
