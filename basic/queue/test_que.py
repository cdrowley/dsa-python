import pytest
from que import Queue  # from queue import Queue defaults to python standard lib version


@pytest.fixture
def setup_queues():
    q = Queue()
    q_with_items = Queue(1, 2, 3, True, None, "ABC")
    return q, q_with_items


def test_queue_init(setup_queues):
    q, q_with_items = setup_queues
    assert list(q) == []
    assert list(q_with_items) == [1, 2, 3, True, None, "ABC"]


def test_isEmpty(setup_queues):
    q, q_with_items = setup_queues
    assert q.isEmpty() == True
    assert q_with_items.isEmpty() == False


def test_size_len(setup_queues):
    q, q_with_items = setup_queues
    assert q.size() == 0
    assert q_with_items.size() == 6
    assert len(q_with_items) == 6


def test_enqueue_dequeue():
    q = Queue()
    assert q.isEmpty() == True

    q.enqueue(4)
    q.enqueue("dog")
    q.enqueue(True)
    assert q.size() == 3
    assert q.isEmpty() == False

    assert q.dequeue() == 4
    assert q.dequeue() == "dog"
    assert q.size() == 1


def test_str(setup_queues):
    q, q_with_items = setup_queues
    assert str(q) == "[]"
    assert str(q_with_items) == "[1, 2, 3, True, None, 'ABC']"


def test_iter(setup_queues):
    q, q_with_items = setup_queues
    q.enqueue(4)
    assert all(True for i in q if i == 4)
    assert all(True for i in q_with_items if i in (1, 2, 3, True, None, "ABC"))
