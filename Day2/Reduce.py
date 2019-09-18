from functools import reduce


def func(a, b):
    return a + b

def largest(a, b):
    return a if a > b else b

def main():
    numbers = [11, 22, 3, 4]
    the_sum = reduce(func, numbers)
    print(the_sum)
    the_sum = reduce(lambda a, b: a + b, numbers)
    print(the_sum)

    large = reduce(largest, numbers)
    print(large)

    large = reduce(lambda a, b: a if a > b else b, numbers)
    print(large)

    small, *_, large = sorted(numbers)
    print(small, large)



if __name__ == '__main__':
    main()
