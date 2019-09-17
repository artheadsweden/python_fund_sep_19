x = 10


def main():
    x = 1
    print(x)
    x += 1

    def inner(): # LEGB
        print(x)

    inner()


if __name__ == '__main__':
    main()
