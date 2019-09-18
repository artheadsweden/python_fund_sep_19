class A:
    def __init__(self):
        print("__init__A")
        self.x = 10


class B(A):
    def __init__(self):
        print("__init__B")
        super().__init__()
        self.x += 1


class C(A):
    def __init__(self):
        print("__init__C")
        super().__init__()
        self.x += 30


class D(C, B):
    def __init__(self):
        print("__init__D")
        super().__init__()


def main():
    d = D()
    print(d.x)
    print(D.__mro__)


if __name__ == '__main__':
    main()
