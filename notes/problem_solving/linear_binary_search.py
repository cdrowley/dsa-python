from util import evaluate_test_cases


def linear_search(values: list, query: int) -> int:  # O(n)
    for idx, value in enumerate(values):
        if value == query:
            return idx
    return -1


def binary_search(lo, hi, condition):  # O(log n)
    """
    General binary search strategy:
        1. Come up with a condition to determine whether the answer lies before, after, or at a given position.
        2. Retrieve the midpoint and middle element of the list.
        3. If the middle element is the answer, return the index.
        4. If the middle element is less than the answer, search the right half of the list.
        5. If the middle element is greater than the answer, search the left half of the list.
    """
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return -1


def locate_value(values: list, query: int) -> int:  # O(log n)
    def condition(mid):
        if values[mid] == query:
            if mid > 0 and values[mid - 1] == query:
                return "left"
            else:
                return "found"
        elif values[mid] < query:
            return "left"
        else:  # values[mid] > query
            return "right"

    return binary_search(0, len(values) - 1, condition)


tests = [
    {"input": {"values": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7}, "output": 3},
    {"input": {"values": [13, 11, 10, 7, 4, 3, 1, 0], "query": 1}, "output": 6},
    {"input": {"values": [4, 2, 1, -1], "query": 4}, "output": 0},
    {"input": {"values": [3, -1, -9, -127], "query": -127}, "output": 3},
    {"input": {"values": [6], "query": 6}, "output": 0},
    {"input": {"values": [9, 7, 5, 2, -9], "query": 4}, "output": -1},
    {"input": {"values": [], "query": 7}, "output": -1},
    {
        "input": {"values": [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query": 3},
        "output": 8,
    },
    {
        "input": {"values": [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query": 6},
        "output": 2,
    },
]

evaluate_test_cases(linear_search, tests)
evaluate_test_cases(locate_value, tests)


def find_start_last_indexes(nums: list, query: int) -> int:
    """Given an array of integers sorted in ascending order, find the start and end indexs of a given number."""

    def find_start_index(nums: list, query: int) -> int:
        def condition(mid):
            if nums[mid] == query:
                if mid > 0 and nums[mid - 1] == query:
                    return "left"
                return "found"
            elif nums[mid] < query:
                return "right"
            else:  # nums[mid] > query
                return "left"

        return binary_search(0, len(nums) - 1, condition)

    def find_last_index(nums: list, query: int) -> int:
        def condition(mid):
            if nums[mid] == query:
                if mid < len(nums) - 1 and nums[mid + 1] == query:
                    return "right"
                return "found"
            elif nums[mid] < query:
                return "right"
            else:  # nums[mid] > query
                return "left"

        return binary_search(0, len(nums) - 1, condition)

    start_index = find_start_index(nums, query)
    last_index = find_last_index(nums, query)
    return start_index, last_index


## NOTES ##

# 1) Clearly state the problem. Identify inputs & outputs.
# 2) Come up with some example inputs & outputs. Try to cover all edge cases.
# 3) Come up with a correct solution for the problem. State it in plain English.
# 4) Implement the solution and test it using example inputs. Fix bugs, if any.
# 5) Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6) Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.


# 3)
# Create a variable position with the value 0.
# Check whether the number at index position in card equals query.
# If it does, position is the answer and can be returned from the function
# If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
# If the number was not found, return -1.
# Linear Search Algorithm: Congratulations, we've just written our first algorithm! An algorithm is simply a list of statements which can be converted into code and executed by a computer on different sets of inputs. This particular algorithm is called linear search, since it involves searching through a list in a linear fashion i.e. element after element.


# 5) linear_locate_card is O(n) because it has to iterate through the entire list. Wheter using a while loop and a position variable or using enumerate, both use O(1) space.


# def recursive_binary_locate_card(cards: list, query: int) -> int:  # O(log n)
#     """
#     Return the index of the card with the given value.
#     If no such card exists, return -1.
#     """
#     if not cards:
#         return -1
#     mid = len(cards) // 2
#     if cards[mid] == query:
#         return mid
#     elif cards[mid] < query:
#         return recursive_locate_card(cards[mid + 1 :], query)
#     else:
#         return recursive_locate_card(cards[:mid], query)
