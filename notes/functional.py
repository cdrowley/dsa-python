# %%
def psum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total


def rsum(numbers):
    if not numbers:
        return 0
    return numbers[0] + rsum(numbers[1:])


print(psum([1, 2, 3, 4, 5]))
print(rsum([1, 2, 3, 4, 5]))


# %%
def dec2bin(d):
    if d < 0:
        raise ValueError("Must be a positive integer.")
    digit = str(d % 2)
    return dec2bin(d // 2) + digit if d > 1 else digit


print(dec2bin(42))
print(dec2bin(0))


def bin2dec(b):
    if b == "":
        return 0
    return int(b[-1]) + 2 * bin2dec(b[:-1])


print(bin2dec("101010"))  # 42
print(bin2dec("0"))  # 0
print(bin2dec("100"))  # 4

print(bin2dec(dec2bin(241212)))
print(dec2bin(241212))
print(dec2bin(bin2dec("111010111000111100")))


# %%
double = lambda x: 2 * x
print(double(12))

iseven = lambda x: x % 2 == 0
print(iseven(12))
print(iseven(13))

isodd = lambda x: not (iseven(x))
print(isodd(13))
print(isodd(12))

# %%
list(map(dec2bin, list(range(16))))

# %%
list(filter(isodd, list(range(16))))

# %%
list(map(dec2bin, (list(filter(isodd, list(range(16)))))))


# %%
from functools import reduce

reduce(lambda x, y: x + y, list(filter(isodd, list(range(100)))))

# %%
reduce(lambda x, y: x * y, list(range(1, 11)))
# %%
