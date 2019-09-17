def func(x):
    return x**2


def main():
    numbers = [1, 2, 3, 4]
    result = list(map(lambda x: x**2, numbers))
    print(result)

    func_fact = lambda e: lambda b: b**e
    square = func_fact(2)
    cube = func_fact(3)

    print(square(3))
    print(cube(3))

if __name__ == '__main__':
    main()
