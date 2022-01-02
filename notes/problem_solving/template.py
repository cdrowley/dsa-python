from util import evaluate_test_cases


def linear_search(values: list, query: int) -> int:  # O(n)
    for idx, value in enumerate(values):
        if value == query:
            return idx
    return -1


tests = [
    {
        "input": {"values": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7},
        "output": 3,
    },  # standard test
    {
        "input": {"values": [13, 11, 10, 7, 4, 3, 1, 0], "query": 1},
        "output": 6,
    },  # standard test
    {
        "input": {"values": [4, 2, 1, -1], "query": 4},
        "output": 0,
    },  # find first item in list
    {
        "input": {"values": [3, -1, -9, -127], "query": -127},
        "output": 3,
    },  # find last item in list
    {"input": {"values": [6], "query": 6}, "output": 0},  # single item list
    {"input": {"values": [], "query": 7}, "output": -1},  # empty list
]

evaluate_test_cases(linear_search, tests)
evaluate_test_cases(locate_value, tests)

# print(locate_value(**test["input"]) == test["output"])

# 1) Clearly state the problem. Identify inputs & outputs.
# 2) Come up with some example inputs & outputs. Try to cover all edge cases.
# 3) Come up with a correct solution for the problem. State it in plain English.
# 4) Implement the solution and test it using example inputs. Fix bugs, if any.
# 5) Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6) Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
