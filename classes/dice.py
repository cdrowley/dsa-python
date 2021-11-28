import random


class MSDie:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.num_sides + 1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)

    def __eq__(self, other) -> bool:
        return self.current_value == other.current_value

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        return self.current_value < other.current_value

    def __gt__(self, other) -> bool:
        return self.current_value > other.current_value

    def __le__(self, other) -> bool:
        return self <= other

    def __ge__(self, other) -> bool:
        return self >= other


if __name__ == '__main__':
    pass