from stack import Stack
import pytest


def parChecker(symbolString, openers="([{", closers=")]}"):
    s = Stack()
    balanced = True
    idx = 0
    while idx < len(symbolString) and balanced:
        symbol = symbolString[idx]
        if symbol in openers:
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not (openers.index(top) == closers.index(symbol)):
                    balanced = False
        idx += 1
    return True if (balanced and s.isEmpty()) else False


def test_parChecker():
    assert parChecker("((()))") == True
    assert parChecker("()") == True

    assert parChecker("(") == False

    assert parChecker("[]", "[", "]") == True
    assert parChecker("[]]", "[", "]") == False

    assert parChecker("bbpp", "b", "p") == True
    assert parChecker("bbppp", "b", "p") == False
    assert parChecker("aaabbb", "a", "b") == True

    assert parChecker("[(())]") == True
    assert parChecker("{({([][])}())}") == True
    assert parChecker("[{()]") == False
