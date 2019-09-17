def func_fact(e):
    def inner(b):
        return b**e
    return inner


def main():
    square = func_fact(2)
    cube = func_fact(3)
    print(square(3))
    print(cube(3))

    funcs = [func_fact(i) for i in range(2, 100)]
    for func in funcs:
        print(func(2))


if __name__ == '__main__':
    main()
