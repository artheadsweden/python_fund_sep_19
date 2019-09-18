class ArgumentError(ValueError):
    pass


def myfunc(x, y):
    if y == 0:
        raise ArgumentError("Argument y can't be 0")
    z = x / y
    return z


def main():
    try:
        result = myfunc(3, 4)
    except ArgumentError as e:
        print(e)
        raise
    except ValueError as e:
        print(e)
    else:
        print(result)
    finally:
        print("Will always execute")

    print("The end")


if __name__ == '__main__':
    main()
