from que import Queue
import pytest


def hotPotato(names: list, num: int) -> str:
    circle = Queue(*names)
    while len(circle) > 1:
        for _ in range(num):
            circle.enqueue(circle.dequeue())
        circle.dequeue()
    return circle.dequeue()


@pytest.mark.parametrize(
    "test, result",
    [
        ((["Brad", "Kent", "Jane", "Susan", "David", "Bill"], 999), "Brad"),
        ((["Brad", "Kent", "Jane", "Susan", "David", "Bill"], 7), "Susan"),
        ((["Brad", "Kent", "Jane", "Susan", "David", "Bill"], 4), "Bill"),
        ((["Brad", "Kent", "Jane", "Susan", "David", "Bill"], 1), "Kent"),
        ((["Brad", "Kent", "Jane", "Susan", "David", "Bill"], 0), "Brad"),
    ],
)
def test_hotPotato(test, result):
    assert hotPotato(*test) == result


if __name__ == '__main__':
    pass