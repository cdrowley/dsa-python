from __future__ import annotations  # not needed in python 3.10
from typing import Union


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise TypeError(
                "Numerator and Denominator of a Fraction must be an integer."
            )

        if denominator == 0:
            raise ZeroDivisionError("The Denominator must not be 0.")

        if numerator == 0:
            self.top, self.bot = 0, 1
            self.numerator, self.denominator = 0, 1
        else:
            if (numerator < 0 and denominator >= 0) or (
                numerator >= 0 and denominator < 0
            ):
                sign = -1
            else:
                sign = 1

            cd = Fraction.gcd(numerator, denominator)
            self.top = sign * (abs(numerator) // cd)
            self.bot = sign * (abs(denominator) // cd)
            self.numerator, self.denominator = numerator, denominator

    @staticmethod
    def gcd(top: int, bot: int) -> int:
        a, b = abs(top), abs(bot)
        while a % b != 0:
            olda, oldb = a, b
            a, b = oldb, olda % oldb
        return b

    def getNum(self) -> int:
        return self.top

    def getDen(self) -> int:
        return self.bot

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.top}, {self.bot})"

    def __str__(self) -> str:
        if self.bot == 1:
            return f"{self.top}"
        elif self.top > self.bot:
            whole = self.top // self.bot
            frac = Fraction(self.top % self.bot, self.bot)
            return f"{whole}  {frac}"
        else:
            return f"{self.top}/{self.bot}"

    def __int__(self) -> int:
        return self.top // self.bot

    def __float__(self) -> float:
        return self.top / self.bot

    def __add__(self, other: Union[int, Fraction]) -> Fraction:
        if isinstance(other, int):
            other = Fraction(other, 1)

        newtop = self.top * other.bot + self.bot * other.top
        newbot = self.bot * other.bot
        return Fraction(newtop, newbot)

    __radd__ = __add__

    def __sub__(self, other: Union[int, Fraction]) -> Fraction:
        if isinstance(other, int):
            other = Fraction(other, 1)

        newtop = self.top * other.bot - self.bot * other.top
        newbot = self.bot * other.bot
        return Fraction(newtop, newbot)

    __rsub__ = __sub__

    def __mul__(self, other: Union[int, Fraction]) -> Fraction:
        if isinstance(other, int):
            other = Fraction(other, 1)

        newtop = self.top * other.top
        newbot = self.bot * other.bot
        return Fraction(newtop, newbot)

    __rmul__ = __mul__

    def __truediv__(self, other: Fraction) -> Fraction:
        newtop = self.top * other.bot
        newbot = self.bot * other.top
        return Fraction(newtop, newbot)

    def __eq__(self, other: Union[int, Fraction]) -> bool:
        return (self.top == other.top) and (self.bot == other.bot)

    def __ne__(self, other: Union[int, Fraction]) -> bool:
        return not self == other

    def __lt__(self, other: Fraction) -> bool:
        return (self.top * other.bot) < (self.bot * other.top)

    def __gt__(self, other: Fraction) -> bool:
        return (self.top * other.bot) > (self.bot * other.top)

    def __le__(self, other: Fraction) -> bool:
        return self <= other

    def __ge__(self, other: Fraction) -> bool:
        return self >= other