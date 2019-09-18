def main():

    gen = (i**2 for i in range(10))
    for i in gen:
        print(i)

    for i in gen:
        print(i)


if __name__ == '__main__':
    main()
