from stack import Stack
import pytest


def parChecker(symbolString, openers="([{", closers=")]}") -> bool:
    """Determines if a string containing various brackets is balanced.

    Pseudocode:
    1. Create a stack.
    2. Scan the each symbol in the input string from left to right.
        a) if the symbol is an "open" bracket then push it onto the stack.
        b) otherwise pop the stack
    3. After scanning, ensure it is empty then return True otherwise False."""

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
