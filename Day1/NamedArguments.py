def func(a, b, c, d=4, e=5):
    print(f"a={a}, b={b}, c={c}")


def main():
    func(1, 2, 3)
    func(c=3, a=1, b=2)
    # print(sep="-", "Hi", 1)


if __name__ == '__main__':
    main()
