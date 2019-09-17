def main():
    numbers = (1, 2, 3, 4, 5, 6)
    one, two, three, four, five, six = numbers
    first, *rest, last = numbers
    print(first)
    print(rest)
    print(last)

    a, *_, b = numbers
    print(a, b)


if __name__ == '__main__':
    main()
