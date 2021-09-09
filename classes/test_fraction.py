import pytest
from fraction import Fraction


@pytest.fixture
def setup_fractions():
    frac_1_3 = Fraction(1, 3)
    frac_5_10 = Fraction(5, 10)
    frac_n2_3 = Fraction(-2, 3)
    return frac_1_3, frac_5_10, frac_n2_3


def test_fraction_init(setup_fractions):
    frac_1_3, frac_5_10, frac_n2_3 = setup_fractions

    assert frac_1_3.numerator == 1
    assert frac_1_3.denominator == 3
    assert frac_1_3.top == 1
    assert frac_1_3.bot == 3

    assert frac_5_10.numerator == 5
    assert frac_5_10.denominator == 10
    assert frac_5_10.top == 1
    assert frac_5_10.bot == 2

    assert frac_n2_3.numerator == -2
    assert frac_n2_3.denominator == 3
    assert frac_n2_3.top == -2
    assert frac_n2_3.bot == -3


def test_no_value():
    with pytest.raises(Exception):
        obj = Fraction()


def test_gcd(setup_fractions):
    frac_1_3, frac_5_10, frac_n2_3 = setup_fractions

    assert Fraction.gcd(1, 2) == 1
    assert Fraction.gcd(2, 4) == 2
    assert Fraction.gcd(3, 9) == 3
    assert Fraction.gcd(7, 140) == 7
    assert Fraction.gcd(80, 80_000) == 80

    assert frac_1_3.gcd(1, 3) == Fraction.gcd(1, 3)

    assert frac_5_10.gcd(frac_5_10.top, frac_5_10.bot) != Fraction.gcd(5, 10)
    assert frac_n2_3.gcd(frac_n2_3.numerator, frac_n2_3.denominator) == Fraction.gcd(
        -2, 3
    )


# tax = Fraction(1, 5)
# stubott_loan = Fraction(9, 100)

# print(tax)
# print(float(tax))
# print(float(tax + stubott_loan))
# print(tax == stubott_loan)
# print(4 + Fraction(3, 5) + 3)

# print(Fraction(3, 1))

# print(Fraction(3, 10) * Fraction(1, 10))
# print(Fraction(1, 2) * Fraction(3, 7))
# print(Fraction(3, 4) < Fraction(1, 2))

# print(Fraction(32, 99) < Fraction(1, 3))

# y = Fraction(1, 2)
# y += Fraction(1, 3)
# print(y)
# # print(Fraction(3, 4) == Fraction(6, 8))
# # print(Fraction(3, 4) == Fraction(6, 8))
# # print(5 * Fraction(1, 2))

# # print(int(Fraction(3, 2)))
