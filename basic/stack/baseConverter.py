from stack import Stack
import pytest


def bin2dec(dec: int) -> str:
    """Simplest Example: Binary to Decimal converter."""
    if dec == 0:
        return "0"

    remainders = Stack()
    while dec > 0:
        rem = dec % 2
        dec = dec // 2
        remainders.push(rem)

    result = ""
    while not remainders.isEmpty():
        result += str(remainders.pop())
    return result


def baseConverter(dec: int, base: int) -> str:
    """Takes a decimal number and converts to any base between 2 and 16."""
    if dec == 0:
        return "0"

    DIGITS = "0123456789ABCDEF"
    remainders = Stack()
    while dec > 0:
        rem = dec % base
        dec = dec // base
        remainders.push(rem)

    return "".join([DIGITS[r] for r in reversed(remainders)])


@pytest.mark.parametrize("test, result", [(233, "11101001"), (42, "101010"), (0, "0")])
def test_bin2dec(test, result):
    assert bin2dec(test) == result


@pytest.mark.parametrize(
    "test, result",
    [((25, 2), "11001"), ((233, 2), "11101001"), ((25, 16), "19"), ((0, 8), "0")],
)
def test_baseConverter(test, result):
    assert baseConverter(*test) == result