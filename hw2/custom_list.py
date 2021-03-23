""" Custom List created by Egor Iudin """


class CustomList(list):
    """ Custom list with new implementation of add, sub and new type of compare """

    def __add__(self, other):
        temp1 = self[:]
        other1 = other[:]
        temp1_len = len(temp1)
        other1_len = len(other1)
        buf = [0]*max(temp1_len, other1_len)

        if temp1_len > other1_len:
            other1 += [0]*(temp1_len - other1_len)
            other1_len = temp1_len
        else:
            temp1 += [0]*(other1_len - temp1_len)
            temp1_len = other1_len

        for i in range(temp1_len):
            buf[i] = temp1[i] + other1[i]

        return CustomList(buf)

    def __radd__(self, other):
        return self.__add__(CustomList(other))

    def __sub__(self, other):
        return self.__add__(CustomList([-1*i for i in other]))

    def __rsub__(self, other):
        return CustomList([-1*i for i in self.__sub__(other)])

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)


if __name__ == "__main__":
    l = CustomList([1, 2, 3])
    d = CustomList([14, -2, 3, 2, 77])
    print(l-d, type(l-d))
    print(d-l, type(d-l))
    r = [1, -55, 66, 99]
    v = [1, -55, 66, 99]
    print(sum(d), sum(r))
    print(l+r, type(l+r))
    print(r+l, type(r+l))
    print(r-d, type(r-d))
    print(d-r, type(d-r))
    print("r == v:", r == v)
    print("r > l:", r > l)
    print("r >= d:", r >= d)
    print("l <= d:", l <= d)
    print("r < v:", r < v)
    print("r != v:", r != v)
