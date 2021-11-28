from basic.linked_list.node import Node
import pytest


def test_Node_init_get_set():
    n = Node(93)
    assert Node.data == 93
    assert Node.getData() == 93

    n.setData(42)
    assert Node.data == 42
    assert Node.getData() == 42


def test_Node_init_get_set():
    n1 = Node("a")
    n2 = Node("b")
    n1.setNext(n2)

    assert n1.getNext() is n2
    assert n1.getNext().getNext() is None

    assert n1.getNext().getData() == "b"
    assert n1.getNext().getData() == n2.getData()