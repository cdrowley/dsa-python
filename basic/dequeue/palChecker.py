from tkinter import FALSE
from deque import Deque
import pytest


def palChecker(string: str) -> bool:
    characters = Deque(*list(string))

    palindrome = True
    while len(characters) > 1 and palindrome:
        first = characters.removeFront()
        last = characters.removeRear()
        if first != last:
            palindrome = False
    return palindrome


@pytest.mark.parametrize(
    "test, result",
    [
        ("lsdkjfskf", False),
        ("abcdecba", False),
        ("abcdcba", True),
        ("abcddcba", True),
        ("radar", True),
        ("a", True),
        ("", True),
    ],
)
def test_palChecker(test, result):
    assert palChecker(test) == result