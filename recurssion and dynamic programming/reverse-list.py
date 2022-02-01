def recReverseList(l: list):
    if l == []:
        return []
    else:
        return [l[-1]] + recReverseList(l[:-1])


if __name__ == "__main__":
    print(recReverseList([1, 2, 3, 4, 5]))
