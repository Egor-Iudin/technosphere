class CustomMeta():
    def __new__(cls, name, bases, attrs):
        to_change = [i for i in attrs if not i.startswith("__")]
        for i in to_change:
            attrs["custom_" + i] = attrs.pop(i)
        return type(name, bases, attrs)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def line(self):
        return 100


if __name__ == "__main__":
    inst = CustomClass()

    print(type(inst))

    print(inst.custom_x)
    print(inst.custom_line())

    inst.x  # ошибка
    inst.line()  # ошибка
