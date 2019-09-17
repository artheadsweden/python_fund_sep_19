def func(*args, **kwargs):
    print(args)
    print(kwargs)


def main():
    func(1, 2, 3)
    func(1, b=3)
    func()


if __name__ == '__main__':
    main()
