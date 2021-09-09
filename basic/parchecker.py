from stack import Stack
import pytest


def parChecker(symbolstring, symbols="()"):
    if not all(True if s in symbols else False for s in symbolstring):
        return False

    s = Stack()
    is_balanced = True
    idx = 0

    while idx < len(symbolstring) and is_balanced:
        symbol = symbolstring[idx]

        if symbol == symbols[0]:
            s.push(symbol)
        else:
            if s.isEmpty():
                is_balanced = False
            else:
                s.pop()
        idx += 1

        return True if is_balanced and s.isEmpty() else False


def test_parChecker():
    assert parChecker("((()))") == True
    assert parChecker("()") == True

    assert parChecker("(") == False
    assert parChecker("((()))") == False

    assert parChecker("[]", "[]") == True
    assert parChecker("[]]", "[]") == False

    assert parChecker("bbbb", "bb") == True
    assert parChecker("a", "aa") == False
