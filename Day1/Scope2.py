def outer(x):
    def inner(y):
        return x + y
    return inner


def main():
    a = outer(120)
    print(a(2))
    b = outer(20)
    print(b(3))
    print(a(4))
    print(b(5))


if __name__ == '__main__':
    main()
